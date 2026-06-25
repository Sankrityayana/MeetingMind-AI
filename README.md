# MeetingMind-AI

An AI-powered Meeting Intelligence Platform that automatically converts meeting audio and video recordings into structured transcripts, summaries, decisions, action items, and searchable knowledge.

## Features

- User authentication and organization support
- Meeting upload and recording capabilities
- AI-powered speech recognition with Whisper
- Automatic transcript generation and summarization
- Action item and decision extraction
- Semantic search and RAG knowledge base
- Calendar and email integrations
- Comprehensive analytics and dashboard
- Export capabilities (PDF, Word, Markdown, CSV, JSON)
- Sharing and collaboration features
- Notifications and reminders

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- Alembic
- JWT
- Celery/FastAPI Background Tasks
- PostgreSQL with pgvector
- Whisper
- Gemini/OpenAI API
- Sentence Transformers

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS
- shadcn/ui
- TanStack Query
- Recharts

### Deployment
- Docker
- Docker Compose
- GitHub Actions
- Vercel/Railway/Render

## Project Structure

```
MeetingMind-AI/
├── backend/
│   ├── app/
│   ├── tests/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── alembic/
├── frontend/
│   ├── app/
│   ├── components/
│   ├── public/
│   ├── styles/
│   ├── package.json
│   └── next.config.js
├── docker-compose.yml
├── .github/
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- PostgreSQL
- Docker & Docker Compose
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sankrityayana/MeetingMind-AI.git
   cd MeetingMind-AI
   ```

2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```bash
   cd ../frontend
   npm install
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Run the application:
   ```bash
   # Backend
   cd backend
   uvicorn app.main:app --reload
   
   # Frontend
   cd ../frontend
   npm run dev
   ```

## Development Phases

This project will be developed in phases:

1. **Phase 1**: Project setup and basic authentication
2. **Phase 2**: Meeting upload and recording functionality
3. **Phase 3**: Speech recognition and transcript generation
4. **Phase 4**: AI processing (summaries, action items, decisions)
5. **Phase 5**: Search and knowledge base features
6. **Phase 6**: Integrations (calendar, email)
7. **Phase 7**: Dashboard and analytics
8. **Phase 8**: Export and sharing capabilities
9. **Phase 9**: Testing, documentation, and deployment
10. **Phase 10**: Production optimization and monitoring

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.