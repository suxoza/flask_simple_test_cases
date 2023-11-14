from flask import Flask, render_template, request, redirect, url_for


class CRUDApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.data = [
            {"id": 1, "name": "item 1"},
            {"id": 2, "name": "item 2"},
            {"id": 3, "name": "item 3"},
        ]
        self.app.add_url_rule("/", "index", self.index)
        self.app.add_url_rule("/add", "add", self.add, methods=["GET", "POST"])
        self.app.add_url_rule(
            "/edit/<int:item_id>", "edit", self.edit, methods=["GET", "POST"]
        )
        self.app.add_url_rule("/delete/<int:item_id>", "delete", self.delete)

    def index(self):
        return render_template("index.html", items=self.data)

    def add(self):
        if request.method == "POST":
            new_item = {"id": len(self.data) + 1, "name": request.form["name"]}
            self.data.append(new_item)
            return redirect(url_for("index"))
        return render_template("add.html")

    def edit(self, item_id):
        item = next((item for item in self.data if item["id"] == int(item_id)), None)
        if request.method == "POST":
            item["name"] = request.form["name"]
            return redirect(url_for("index"))
        return render_template("edit.html", item=item)

    def delete(self, item_id):
        self.data = [item for item in self.data if item["id"] != item_id]
        return redirect(url_for("index"))

    def run(self):
        self.app.run(debug=True)


if __name__ == "__main__":
    crud_app = CRUDApp()
    crud_app.run()
