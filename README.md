# API Football SDK

This project provides an SDK for interacting with the **API Football** service, enabling the retrieval and analysis of football data across various competitions, such as the **Copa Libertadores**, **Copa do Brasil**, and **Copa Sudamericana**.
The goal is to offer a solid and structured Python interface to fetch, filter, and analyze data for content creation and statistical insights, especially for bettors and sports analysts.

## 📦 Project Structure

- `src/api_football_sdk/`
  - Core package with all SDK functionalities.
  - `client.py`: HTTP client abstraction with retry logic.
  - `config.py`: Runtime settings management.
  - `exceptions.py`: Custom exception hierarchy.
  - `models.py`: (Reserved for future typed models.)
  - `adapters/`: Extensible adapter base classes.
  - `endpoints/`: Modular implementation for each API Football endpoint.
- `tests/`
  - Full unit and integration test coverage, using `pytest` and `respx`.
- `.pre-commit-config.yaml`
  - Pre-commit hooks configuration for formatting and linting.
- `noxfile.py`
  - Automated sessions for testing, linting, formatting, and coverage.
- `pyproject.toml`
  - Project metadata, dependencies, and tool configurations.
- `README.md`, `LICENSE`, `CHANGELOG.md`
  - Documentation and licensing information.

## ⚙️ Requirements

- Python 3.10+
- Install dependencies:

```bash
pip install ".[dev]"
```

## 🚀 Usage

1. Configure your API key by setting the environment variable `API_FOOTBALL_KEY`, or create a `.env` file at the project root:

```bash
API_FOOTBALL_KEY=your_rapidapi_key
```

2. Example usage to retrieve fixtures:

```python
from api_football_sdk.endpoints.fixtures import get_fixtures_by_league
import asyncio

async def main():
    fixtures = await get_fixtures_by_league(league_id=13, season=2024)
    print(fixtures)

asyncio.run(main())
```

## 🧪 Running Tests

You can run all tests with:

```bash
nox -s tests
```

Or manually using `pytest`:

```bash
pytest
```

Coverage report:

```bash
nox -s coverage
```

HTML coverage report will be generated under the `htmlcov/` directory.

## 🚲 Development Setup

Recommended development steps:

```bash
pre-commit install
nox
```

This will automatically run formatters (`black`, `ruff`), linters, and tests during commits and local development.

## 👢 Endpoints Implemented

The following API Football endpoints are currently implemented:

- **Timezones**
- **Predictions**
- **Fixtures** (Games)
- **Events** (Goals, cards, substitutions)
- **Statistics** (Match statistics)
- **Lineups** (Starting XI)
- **Standings** (League tables)
- **Leagues** (Competition data)
- **Trophies** (Player and coach titles)
- **Teams** (Team metadata and statistics)
- **Players** (Player metadata, stats, history)
- **Coaches** (Coach metadata)
- **Transfers** (Player transfers)
- **Injuries** (Injury reports)
- **Sidelined** (Unavailable players)
- **Top Scorers** (Goals, assists, cards)
- **Venues** (Stadiums)
- **Countries and Seasons** (Reference data)
- **Search** (Search functionality)

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 📢 Contributions

Contributions, feature requests, and bug reports are welcome! Feel free to open issues or submit pull requests.

# ✨ Future Improvements

- Typed models with Pydantic for endpoint responses.
- Advanced retry policies and circuit breaking.
- Typed pagination helpers.
