from flask import Blueprint, render_template

docs_v1 = Blueprint("docs", __name__, url_prefix="/docs")

@docs_v1.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template('/docs/index.html')

@docs_v1.route('/stories', methods=['GET'], strict_slashes=False)
def stories():
    return render_template('/docs/stories.html')