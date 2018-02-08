# coding=utf-8
from flask import jsonify

from pysite.base_route import RouteView


class IndexView(RouteView):
    path = "/healthcheck"
    name = "healthcheck"

    def get(self):
        return jsonify({"status": "ok"})
