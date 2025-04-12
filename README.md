# SmartHire

SmartHire is a multi-agent recruitment application designed to automate the recruitment process. It provides functionalities for summarizing job descriptions, parsing CVs, matching candidates, and sending interview requests.

## Features

- **Job Description Summarization**: Summarizes job descriptions from a CSV file.
- **CV Parsing**: Extracts text from PDF CVs using PyPDF2.
- **Candidate Matching**: Calculates match scores between job descriptions and CVs using scikit-learn.
- **Email Sending**: Sends interview requests via email.

## Getting Started

### Prerequisites

- Docker
- Python 3.9

### Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd IS_HACK
   ```

2. **Build the Docker Image**
   ```bash
   docker build -t smarthire .
   ```

3. **Run the Docker Container**
   ```bash
   docker run -p 8000:8000 smarthire
   ```

### API Endpoints

- `POST /summarize_jd/`: Summarizes job descriptions from a CSV file.
- `POST /parse_cv/`: Parses CVs from PDF files.
- `POST /match_candidates/`: Matches candidates to job descriptions.
- `POST /send_email/`: Sends interview requests via email.

### Deployment

To deploy the application on a cloud platform like Render, follow the steps provided in the deployment guide.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please contact [your-email@example.com].
