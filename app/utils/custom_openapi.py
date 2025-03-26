from fastapi.openapi.utils import get_openapi


def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Vellubra",
        version="0.0.1",
        description="Allows users to manage their notes.\n\n# **⚠️ This API is still in beta. 🛠️**\n\n## **Features:**\n- Async multiple devices\n- Can be published\n## **TODO**:\n- ✅ Basic notes.\n- ✅ Authentication.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema
