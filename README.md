
# Vellubra API

> # ***"Wherein thoughts be preserved, and knowledge endureth." —***


Vellubra is a **ledger of musings**, a repository wherein one may **scribe notes** (note-taking API) with the prospect of **supporting markdown** anon. It shall soon bestow the boon of **synchrony ‘twixt web and mobile**, and verily, the author may **proclaim their writings for all to see**.

***This repository containeth but the API** the web and mobile countenances shall be wrought in due course.*

## Boons Bestowed Upon Thee (Features)
- [x] Inscription and safekeeping of text (notes)
- [x] Authentication by way of **Bearer Token (JWT) and bcrypt**
- [x] **RapiDoc** doth furnish the documentation
- [ ] Support for markdown
- [ ] Public sharing of manuscripts

## To Set Forth This System (Installation)
### That Which Is Required (Prerequisites)
- `Python 3.x`
- `pip` *(the gatherer of dependencies)*
### The Ritual (Steps)
#### 1. Procure the repository:
```sh
git clone https://github.com/yourusername/vellubra.git
cd vellubra
```
#### 2. Invoke a virtual environment (optional yet sagacious):
```sh
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
#### 3. Gather the dependencies:
```sh
pip install -r requirements.txt
```
#### 4. Configure thine environment:
- Copy `.env.example` unto `.env` and set it aright.
#### 5. Summon the API:
```sh
fastapi dev
```
#### 6. Behold the documentation:
- RapiDoc UI: `http://127.0.0.1:8000/`
- Alternative RapiDoc Path: `http://127.0.0.1:8000/rapidoc`

## Of Its Purpose and Manner (Usage)

Hitherto, the API permitteth:
- **Authentication** through **Bearer Token (JWT) & bcrypt**
- **Scribing and keeping of notes** (text only as of now)

## That Which Shall Come to Pass (Planned Features)
- Markdown’s embrace (to be rendered by the frontend, yet stored as-is)
- The heralding of public notes unto the world

## That Which Doth Uphold This Work (Technology Stack)
- **Tongue of the Machine (Backend):** Python + FastAPI
- **Keeper of Knowledge (Database):** SQLite (soon to be Supabase)
- **The Architect (ORM):** SQLModel
- **Sentinel of the Gates (Authentication):** JWT + bcrypt

## The Manner of Its Configuration (Configuration)
- Uses `.env` to shelter secrets.
- All dependencies must be gathered from `requirements.txt` ere one may proceed.

## Of Trials and Tribulations (Testing)
***Yet unbuilt! It shall be wrought in due time!***