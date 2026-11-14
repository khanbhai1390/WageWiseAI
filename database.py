
import sqlite3

DATABASE_NAME = "wagewise.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS audits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            worker_name TEXT NOT NULL,
            employer TEXT,
            payment_model TEXT,
            hours_worked REAL DEFAULT 0,
            hourly_rate REAL DEFAULT 0,
            deliveries INTEGER DEFAULT 0,
            rate_per_delivery REAL DEFAULT 0,
            expected_bonus REAL DEFAULT 0,
            agreed_deductions REAL DEFAULT 0,
            actual_payment REAL DEFAULT 0,
            expected_gross REAL DEFAULT 0,
            expected_net REAL DEFAULT 0,
            discrepancy REAL DEFAULT 0,
            status TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_audit(data, calculation):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO audits (
            worker_name, employer, payment_model,
            hours_worked, hourly_rate, deliveries,
            rate_per_delivery, expected_bonus,
            agreed_deductions, actual_payment,
            expected_gross, expected_net,
            discrepancy, status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["worker_name"],
        data.get("employer", ""),
        data["payment_model"],
        data.get("hours_worked", 0),
        data.get("hourly_rate", 0),
        data.get("deliveries", 0),
        data.get("rate_per_delivery", 0),
        data.get("expected_bonus", 0),
        data.get("agreed_deductions", 0),
        data["actual_payment"],
        calculation["expected_gross"],
        calculation["expected_net"],
        calculation["discrepancy"],
        calculation["status"]
    ))

    audit_id = cursor.lastrowid
    connection.commit()
    connection.close()

    return audit_id


def get_all_audits():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM audits ORDER BY id DESC")
    audits = cursor.fetchall()

    connection.close()
    return audits


def get_audit(audit_id):
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM audits WHERE id = ?", (audit_id,))
    audit = cursor.fetchone()

    connection.close()
    return audit
