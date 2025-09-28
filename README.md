# SBD Checker API

A FastAPI service to check AWS member SBD assignments using Supabase as the backend database.

## Features

- Look up SBD department by AWS CCID
- Fast API with automatic documentation
- Type-safe responses with Pydantic models
- Supabase integration for data retrieval
- Proper error handling and null value support

## Prerequisites

- Python 3.10 or higher
- A Supabase project with an `aws_members` table

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/thatjohnlagman/sbd_checker.git
   cd sbd_checker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Create a `.env` file** in the project root directory:
   ```bash
   touch .env
   ```

2. **Add your Supabase credentials** to the `.env` file:
   ```env
   SUPABASE_URL=your_supabase_project_url
   SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key
   ```

   You can find these values in your Supabase project dashboard:
   - **SUPABASE_URL**: Go to Settings → API → Project URL
   - **SUPABASE_SERVICE_ROLE_KEY**: Go to Settings → API → Project API keys → service_role

## Database Schema

Ensure your Supabase database has an `aws_members` table with the following structure:

```sql
CREATE TABLE aws_members (
    awsccid TEXT PRIMARY KEY,
    sbd_dept TEXT
);
```

## Usage

1. **Start the development server**
   ```bash
   fastapi dev main.py
   ```

2. **Access the API**
   - API Base URL: `http://localhost:8000`
   - Interactive Documentation: `http://localhost:8000/docs`
   - Alternative Documentation: `http://localhost:8000/redoc`

## API Endpoints

### GET `/check_sbd/{awsccid}`

Check the SBD department for a given AWS CCID.

**Parameters:**
- `awsccid` (string): The AWS CCID to look up

**Response Examples:**

✅ **Success (with SBD department):**
```json
{
  "sbd_dept": "Engineering"
}
```

✅ **Success (no SBD department assigned):**
```json
{
  "sbd_dept": null
}
```

❌ **Error (AWSCCID not found):**
```json
{
  "error": "No member found with AWSCCID: 'invalid123'"
}
```

❌ **Error (Database error):**
```json
{
  "error": "Unexpected error: Connection failed"
}
```

## Development

The API uses:
- **FastAPI** for the web framework
- **Supabase** for database operations
- **Pydantic** for data validation and serialization
- **python-dotenv** for environment variable management

## Project Structure

```
sbd_checker/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (create this)
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
