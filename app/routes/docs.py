from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
@router.get("/rapidoc", response_class=HTMLResponse, include_in_schema=False)
async def rapidoc():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <script type="module" src="https://unpkg.com/rapidoc/dist/rapidoc-min.js"></script>
        </head>
        <body>
            <rapi-doc spec-url="/openapi.json" show-info="true" show-curl-before-try="true" allow-server-selection="false" allow-search="true" theme="light" render-style="focused" primary-color="#34A853" show-header="false"></rapi-doc>
        </body>
    </html>
    """
