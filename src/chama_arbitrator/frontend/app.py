"""Chama Arbitrator - Streamlit Frontend

A multilingual chat interface for AI-powered dispute resolution in Kenyan Chamas.
Supports document uploads, conversation history, and arbitration rulings.
"""

import streamlit as st
import requests
import json
import os
from typing import Optional, Dict, Any
from datetime import datetime


# ============================================================================
# Configuration & Initialization
# ============================================================================

st.set_page_config(
    page_title="⚖️ Chama Arbitrator",
    layout="wide",
    initial_sidebar_state="expanded"
)

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


def initialize_session_state() -> None:
    """Initialize Streamlit session state for chat and uploads."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "uploaded_documents" not in st.session_state:
        st.session_state.uploaded_documents = []
    if "session_id" not in st.session_state:
        st.session_state.session_id = datetime.now().isoformat()


initialize_session_state()


# ============================================================================
# Helper Functions
# ============================================================================

async def send_query_to_backend(
    query: str,
    context_documents: Optional[list] = None
) -> Dict[str, Any]:
    """Send user query to backend and get arbitration response.

    Args:
        query: User's question or dispute description.
        context_documents: List of uploaded document paths for context.

    Returns:
        Response dictionary with ruling and metadata.
    """
    try:
        payload = {
            "query": query,
            "session_id": st.session_state.session_id,
            "context": {
                "uploaded_documents": context_documents or [],
                "message_count": len(st.session_state.messages)
            }
        }

        response = requests.post(
            f"{BACKEND_URL}/resolve",
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.ConnectionError:
        return {
            "error": "Backend connection failed",
            "message": f"Unable to connect to {BACKEND_URL}. Is the server running?"
        }
    except requests.exceptions.Timeout:
        return {
            "error": "Request timeout",
            "message": "Backend took too long to respond. Try again."
        }
    except Exception as e:
        return {
            "error": "Request failed",
            "message": str(e)
        }


def save_uploaded_file(uploaded_file) -> str:
    """Save uploaded file to a temporary location and return path.

    Args:
        uploaded_file: Streamlit UploadedFile object.

    Returns:
        Path to saved file or error message.
    """
    try:
        # Create uploads directory if it doesn't exist
        os.makedirs("data/uploads", exist_ok=True)

        file_path = os.path.join("data/uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        return file_path
    except Exception as e:
        return f"Error saving file: {str(e)}"


def format_message_display(role: str, content: str) -> str:
    """Format message for display with role indicator.

    Args:
        role: Message role ('user' or 'assistant').
        content: Message content.

    Returns:
        Formatted message string.
    """
    if role == "user":
        return f"👤 **You**: {content}"
    else:
        return f"⚖️ **Arbitrator**: {content}"


# ============================================================================
# UI Layout
# ============================================================================

# Header
st.markdown("# ⚖️ Chama Arbitrator")
st.markdown("### Neutral Dispute Resolution for Your Cooperative")
st.markdown("---")

# Sidebar for settings and document management
with st.sidebar:
    st.header("📋 Document Management")

    uploaded_file = st.file_uploader(
        "Upload Chama Bylaws (PDF, TXT, or CSV)",
        type=["pdf", "txt", "csv"],
        help="Upload your chama bylaws or membership documents for context"
    )

    if uploaded_file is not None:
        with st.spinner("Processing document..."):
            file_path = save_uploaded_file(uploaded_file)
            if not file_path.startswith("Error"):
                st.session_state.uploaded_documents.append({
                    "name": uploaded_file.name,
                    "path": file_path,
                    "size": uploaded_file.size,
                    "uploaded_at": datetime.now().isoformat()
                })
                st.success(f"✅ Uploaded: {uploaded_file.name}")
            else:
                st.error(file_path)

    if st.session_state.uploaded_documents:
        st.subheader("📂 Uploaded Documents")
        for doc in st.session_state.uploaded_documents:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.caption(f"📄 {doc['name']}")
            with col2:
                if st.button("❌", key=f"remove_{doc['name']}"):
                    st.session_state.uploaded_documents.remove(doc)
                    st.rerun()

    st.divider()
    st.subheader("⚙️ Settings")

    language = st.selectbox(
        "Preferred Language",
        ["English", "Swahili", "Sheng"],
        help="Language for responses"
    )

    tone = st.selectbox(
        "Response Tone",
        ["Formal", "Professional", "Neutral"],
        index=2,
        help="Tone of arbitration ruling"
    )

    if st.button("🔄 Clear Conversation"):
        st.session_state.messages = []
        st.success("Conversation cleared")
        st.rerun()


# Main chat area
st.subheader("💬 Dispute Resolution Chat")

# Display conversation history
for message in st.session_state.messages:
    with st.container():
        if message["role"] == "user":
            st.write(format_message_display("user", message["content"]))
        else:
            # Display assistant response with ruling details
            st.write(format_message_display("assistant", message["content"]))
            if "metadata" in message:
                with st.expander("📊 View Details"):
                    if "confidence" in message["metadata"]:
                        st.metric("Confidence Score", f"{message['metadata']['confidence']:.1%}")
                    if "sources" in message["metadata"]:
                        st.caption(f"**Sources**: {', '.join(message['metadata']['sources'])}")
                    if "analysis_time" in message["metadata"]:
                        st.caption(f"**Analysis Time**: {message['metadata']['analysis_time']:.2f}s")
        st.divider()


# Input area
col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_area(
        "Enter your dispute or question",
        placeholder="Describe your dispute or ask about chama bylaws (Sheng, Swahili, or English)...",
        height=100,
        label_visibility="collapsed"
    )

with col2:
    submit_button = st.button(
        "🚀 Submit",
        type="primary",
        use_container_width=True
    )

# Process user input
if submit_button and user_input:
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Show processing indicator
    with st.spinner("⏳ Arbitrator is analyzing your case..."):
        # Prepare document context
        doc_paths = [doc["path"] for doc in st.session_state.uploaded_documents]

        # Call backend
        response = send_query_to_backend(user_input, doc_paths)

        # Handle response
        if "error" in response:
            st.error(f"**Error**: {response['message']}")
        else:
            # Extract response data
            ruling = response.get("ruling", "No ruling generated")
            metadata = response.get("metadata", {})

            # Add assistant message to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": ruling,
                "metadata": metadata
            })

            # Display the response
            st.success("✅ Arbitration Complete")
            st.write(format_message_display("assistant", ruling))

            if metadata:
                with st.expander("📊 View Details"):
                    if "confidence" in metadata:
                        st.metric("Confidence Score", f"{metadata['confidence']:.1%}")
                    if "sources" in metadata:
                        st.caption(f"**Sources**: {', '.join(metadata['sources'])}")
                    if "analysis_time" in metadata:
                        st.caption(f"**Analysis Time**: {metadata['analysis_time']:.2f}s")

elif submit_button:
    st.warning("⚠️ Please enter a query before submitting")


# Footer
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 0.9em;'>
    <p>⚖️ Chama Arbitrator - Powered by AI Agents</p>
    <p>Confidential & Impartial Dispute Resolution</p>
    </div>
    """,
    unsafe_allow_html=True
)
