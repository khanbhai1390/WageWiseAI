
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    abort,
    send_file
)

from database import (
    create_database,
    save_audit,
    get_all_audits,
    get_audit
)

from wage_engine import calculate_wage
from report_generator import generate_report

app = Flask(__name__)

# Create database
create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/new-audit", methods=["GET", "POST"])
def new_audit():

    if request.method == "POST":

        data = {
            "worker_name": request.form.get("worker_name", "").strip(),
            "employer": request.form.get("employer", "").strip(),
            "payment_model": request.form.get("payment_model", ""),
            "hours_worked": request.form.get("hours_worked") or 0,
            "hourly_rate": request.form.get("hourly_rate") or 0,
            "deliveries": request.form.get("deliveries") or 0,
            "rate_per_delivery": request.form.get("rate_per_delivery") or 0,
            "expected_bonus": request.form.get("expected_bonus") or 0,
            "agreed_deductions": request.form.get("agreed_deductions") or 0,
            "actual_payment": request.form.get("actual_payment") or 0
        }

        if not data["worker_name"] or not request.form.get("actual_payment"):
            return render_template(
                "audit.html",
                error="Please enter the worker name and actual payment."
            )

        try:
            calculation = calculate_wage(data)
            audit_id = save_audit(data, calculation)

            return redirect(
                url_for("view_audit", audit_id=audit_id)
            )

        except (ValueError, KeyError) as error:
            return render_template(
                "audit.html",
                error=str(error)
            )

    return render_template("audit.html")


@app.route("/result/<int:audit_id>")
def view_audit(audit_id):

    audit = get_audit(audit_id)

    if audit is None:
        abort(404)

    return render_template("result.html", audit=audit)


@app.route("/dashboard")
def dashboard():

    audits = get_all_audits()

    return render_template(
        "dashboard.html",
        audits=audits
    )


# Download individual earnings report
@app.route("/download-report/<int:audit_id>")
def download_report(audit_id):

    audit = get_audit(audit_id)

    if audit is None:
        abort(404)

    report_path = generate_report(audit)

    return send_file(
        report_path,
        as_attachment=True,
        download_name=f"WageWise_AI_Report_{audit_id}.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)
