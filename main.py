import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


# ============================================================
# DATA STORAGE
# ============================================================

patients = []

appointments = []

doctors = [
    {
        "name": "Dr. John Smith",
        "specialty": "General Medicine"
    },
    {
        "name": "Dr. Sarah Williams",
        "specialty": "Pediatrics"
    },
    {
        "name": "Dr. Michael Brown",
        "specialty": "Cardiology"
    },
    {
        "name": "Dr. Emily Davis",
        "specialty": "Dermatology"
    }
]

available_slots = [
    "09:00 AM",
    "10:00 AM",
    "11:00 AM",
    "01:00 PM",
    "02:00 PM",
    "03:00 PM",
    "04:00 PM"
]


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Hospital Management System")

root.geometry("1100x700")

root.minsize(900, 600)

root.configure(bg="#f4f6f8")


# ============================================================
# COLORS
# ============================================================

PRIMARY = "#1f6f8b"
SECONDARY = "#145374"
LIGHT = "#eef5f7"
WHITE = "#ffffff"
DARK = "#263238"
SUCCESS = "#2e7d32"
DANGER = "#c62828"


# ============================================================
# GENERAL FUNCTIONS
# ============================================================

def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()


def create_title(parent, title, subtitle=""):
    title_label = tk.Label(
        parent,
        text=title,
        font=("Arial", 24, "bold"),
        bg=WHITE,
        fg=DARK
    )

    title_label.pack(anchor="w", padx=30, pady=(25, 5))

    if subtitle:
        subtitle_label = tk.Label(
            parent,
            text=subtitle,
            font=("Arial", 11),
            bg=WHITE,
            fg="#607d8b"
        )

        subtitle_label.pack(anchor="w", padx=30, pady=(0, 20))


def create_button(parent, text, command):
    return tk.Button(
        parent,
        text=text,
        command=command,
        font=("Arial", 11, "bold"),
        bg=PRIMARY,
        fg=WHITE,
        activebackground=SECONDARY,
        activeforeground=WHITE,
        relief="flat",
        cursor="hand2",
        padx=15,
        pady=8
    )


# ============================================================
# DASHBOARD HOME
# ============================================================

def show_home():

    clear_content()

    create_title(
        content_frame,
        "Hospital Management System",
        "Welcome to the hospital administration system"
    )

    dashboard_frame = tk.Frame(
        content_frame,
        bg=WHITE
    )

    dashboard_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=10
    )

    # Patient card
    patient_card = tk.Frame(
        dashboard_frame,
        bg=LIGHT,
        padx=25,
        pady=20
    )

    patient_card.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    tk.Label(
        patient_card,
        text="Registered Patients",
        font=("Arial", 12, "bold"),
        bg=LIGHT,
        fg=DARK
    ).pack()

    tk.Label(
        patient_card,
        text=str(len(patients)),
        font=("Arial", 30, "bold"),
        bg=LIGHT,
        fg=PRIMARY
    ).pack(pady=10)

    # Appointment card
    appointment_card = tk.Frame(
        dashboard_frame,
        bg=LIGHT,
        padx=25,
        pady=20
    )

    appointment_card.grid(
        row=0,
        column=1,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    tk.Label(
        appointment_card,
        text="Appointments",
        font=("Arial", 12, "bold"),
        bg=LIGHT,
        fg=DARK
    ).pack()

    tk.Label(
        appointment_card,
        text=str(len(appointments)),
        font=("Arial", 30, "bold"),
        bg=LIGHT,
        fg=PRIMARY
    ).pack(pady=10)

    # Doctors card
    doctor_card = tk.Frame(
        dashboard_frame,
        bg=LIGHT,
        padx=25,
        pady=20
    )

    doctor_card.grid(
        row=0,
        column=2,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    tk.Label(
        doctor_card,
        text="Doctors",
        font=("Arial", 12, "bold"),
        bg=LIGHT,
        fg=DARK
    ).pack()

    tk.Label(
        doctor_card,
        text=str(len(doctors)),
        font=("Arial", 30, "bold"),
        bg=LIGHT,
        fg=PRIMARY
    ).pack(pady=10)

    dashboard_frame.columnconfigure(0, weight=1)
    dashboard_frame.columnconfigure(1, weight=1)
    dashboard_frame.columnconfigure(2, weight=1)

    info = tk.Label(
        content_frame,
        text=(
            "Use the menu on the left to register patients, "
            "book appointments, access patient records, "
            "and manage doctor information."
        ),
        font=("Arial", 12),
        bg=WHITE,
        fg="#455a64",
        wraplength=800,
        justify="left"
    )

    info.pack(anchor="w", padx=40, pady=30)


# ============================================================
# PATIENT REGISTRATION
# ============================================================

def show_patient_registration():

    clear_content()

    create_title(
        content_frame,
        "Patient Registration",
        "Enter patient information carefully"
    )

    form = tk.Frame(
        content_frame,
        bg=WHITE
    )

    form.pack(
        padx=40,
        pady=10,
        fill="x"
    )

    # Variables
    patient_id_var = tk.StringVar()
    name_var = tk.StringVar()
    age_var = tk.StringVar()
    gender_var = tk.StringVar()
    phone_var = tk.StringVar()
    address_var = tk.StringVar()

    # Patient ID
    tk.Label(
        form,
        text="Patient ID *",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=DARK
    ).grid(row=0, column=0, sticky="w", pady=10)

    patient_id_entry = tk.Entry(
        form,
        textvariable=patient_id_var,
        font=("Arial", 11),
        width=40
    )

    patient_id_entry.grid(
        row=0,
        column=1,
        padx=20,
        pady=10
    )

    # Full Name
    tk.Label(
        form,
        text="Full Name *",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=DARK
    ).grid(row=1, column=0, sticky="w", pady=10)

    name_entry = tk.Entry(
        form,
        textvariable=name_var,
        font=("Arial", 11),
        width=40
    )

    name_entry.grid(
        row=1,
        column=1,
        padx=20,
        pady=10
    )

    # Age
    tk.Label(
        form,
        text="Age *",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=DARK
    ).grid(row=2, column=0, sticky="w", pady=10)

    age_entry = tk.Entry(
        form,
        textvariable=age_var,
        font=("Arial", 11),
        width=40
    )

    age_entry.grid(
        row=2,
        column=1,
        padx=20,
        pady=10
    )

    # Gender
    tk.Label(
        form,
        text="Gender *",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=DARK
    ).grid(row=3, column=0, sticky="w", pady=10)

    gender_combo = ttk.Combobox(
        form,
        textvariable=gender_var,
        values=["Male", "Female", "Other"],
        state="readonly",
        width=37,
        font=("Arial", 11)
    )

    gender_combo.grid(
        row=3,
        column=1,
        padx=20,
        pady=10
    )

    # Phone
    tk.Label(
        form,
        text="Phone Number *",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=DARK
    ).grid(row=4, column=0, sticky="w", pady=10)

    phone_entry = tk.Entry(
        form,
        textvariable=phone_var,
        font=("Arial", 11),
        width=40
    )

    phone_entry.grid(
        row=4,
        column=1,
        padx=20,
        pady=10
    )

    # Address
    tk.Label(
        form,
        text="Address *",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=DARK
    ).grid(row=5, column=0, sticky="w", pady=10)

    address_entry = tk.Entry(
        form,
        textvariable=address_var,
        font=("Arial", 11),
        width=40
    )

    address_entry.grid(
        row=5,
        column=1,
        padx=20,
        pady=10
    )

    # Validation and registration
    def register_patient():

        patient_id = patient_id_var.get().strip()
        name = name_var.get().strip()
        age = age_var.get().strip()
        gender = gender_var.get().strip()
        phone = phone_var.get().strip()
        address = address_var.get().strip()

        # Required fields
        if not all([patient_id, name, age, gender, phone, address]):
            messagebox.showerror(
                "Validation Error",
                "Please fill in all required fields."
            )
            return

        # Patient ID duplicate check
        for patient in patients:
            if patient["id"] == patient_id:
                messagebox.showerror(
                    "Validation Error",
                    "This Patient ID already exists."
                )
                return

        # Age validation
        try:
            age_number = int(age)

            if age_number <= 0 or age_number > 120:
                messagebox.showerror(
                    "Validation Error",
                    "Age must be between 1 and 120."
                )
                return

        except ValueError:
            messagebox.showerror(
                "Validation Error",
                "Age must contain numbers only."
            )
            return

        # Phone validation
        if not phone.isdigit():
            messagebox.showerror(
                "Validation Error",
                "Phone number must contain numbers only."
            )
            return

        if len(phone) < 10:
            messagebox.showerror(
                "Validation Error",
                "Please enter a valid phone number."
            )
            return

        # Save patient
        patient = {
            "id": patient_id,
            "name": name,
            "age": age_number,
            "gender": gender,
            "phone": phone,
            "address": address
        }

        patients.append(patient)

        messagebox.showinfo(
            "Registration Successful",
            f"Patient {name} has been registered successfully."
        )

        # Clear form
        patient_id_var.set("")
        name_var.set("")
        age_var.set("")
        gender_var.set("")
        phone_var.set("")
        address_var.set("")

    button_frame = tk.Frame(
        content_frame,
        bg=WHITE
    )

    button_frame.pack(
        padx=40,
        pady=20,
        anchor="w"
    )

    register_button = create_button(
        button_frame,
        "Register Patient",
        register_patient
    )

    register_button.pack(side="left", padx=(0, 10))

    clear_button = tk.Button(
        button_frame,
        text="Clear",
        command=lambda: [
            patient_id_var.set(""),
            name_var.set(""),
            age_var.set(""),
            gender_var.set(""),
            phone_var.set(""),
            address_var.set("")
        ],
        font=("Arial", 11, "bold"),
        bg="#78909c",
        fg=WHITE,
        relief="flat",
        cursor="hand2",
        padx=20,
        pady=8
    )

    clear_button.pack(side="left")


# ============================================================
# APPOINTMENT BOOKING
# ============================================================

def show_appointment_booking():

    clear_content()

    create_title(
        content_frame,
        "Appointment Booking",
        "Search for a doctor and select an available appointment"
    )

    form = tk.Frame(
        content_frame,
        bg=WHITE
    )

    form.pack(
        padx=40,
        pady=10,
        fill="x"
    )

    patient_var = tk.StringVar()
    doctor_var = tk.StringVar()
    date_var = tk.StringVar()
    time_var = tk.StringVar()

    # Patient
    tk.Label(
        form,
        text="Patient *",
        font=("Arial", 11, "bold"),
        bg=WHITE
    ).grid(row=0, column=0, sticky="w", pady=10)

    patient_names = [
        f"{p['id']} - {p['name']}"
        for p in patients
    ]

    patient_combo = ttk.Combobox(
        form,
        textvariable=patient_var,
        values=patient_names,
        state="readonly",
        width=38
    )

    patient_combo.grid(
        row=0,
        column=1,
        padx=20,
        pady=10
    )

    # Doctor
    tk.Label(
        form,
        text="Doctor *",
        font=("Arial", 11, "bold"),
        bg=WHITE
    ).grid(row=1, column=0, sticky="w", pady=10)

    doctor_names = [
        f"{doctor['name']} - {doctor['specialty']}"
        for doctor in doctors
    ]

    doctor_combo = ttk.Combobox(
        form,
        textvariable=doctor_var,
        values=doctor_names,
        state="readonly",
        width=38
    )

    doctor_combo.grid(
        row=1,
        column=1,
        padx=20,
        pady=10
    )

    # Date
    tk.Label(
        form,
        text="Date *",
        font=("Arial", 11, "bold"),
        bg=WHITE
    ).grid(row=2, column=0, sticky="w", pady=10)

    date_entry = tk.Entry(
        form,
        textvariable=date_var,
        width=40
    )

    date_entry.grid(
        row=2,
        column=1,
        padx=20,
        pady=10
    )

    tk.Label(
        form,
        text="Format: YYYY-MM-DD",
        font=("Arial", 9),
        fg="#78909c",
        bg=WHITE
    ).grid(
        row=2,
        column=2,
        sticky="w"
    )

    # Time
    tk.Label(
        form,
        text="Available Time *",
        font=("Arial", 11, "bold"),
        bg=WHITE
    ).grid(row=3, column=0, sticky="w", pady=10)

    time_combo = ttk.Combobox(
        form,
        textvariable=time_var,
        values=available_slots,
        state="readonly",
        width=38
    )

    time_combo.grid(
        row=3,
        column=1,
        padx=20,
        pady=10
    )

    # Available slots
    slots_frame = tk.LabelFrame(
        content_frame,
        text="Available Time Slots",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=DARK,
        padx=15,
        pady=15
    )

    slots_frame.pack(
        padx=40,
        pady=20,
        fill="x"
    )

    for slot in available_slots:
        tk.Label(
            slots_frame,
            text=slot,
            bg=LIGHT,
            fg=PRIMARY,
            font=("Arial", 10, "bold"),
            padx=15,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

    def book_appointment():

        patient = patient_var.get().strip()
        doctor = doctor_var.get().strip()
        date = date_var.get().strip()
        time = time_var.get().strip()

        if not all([patient, doctor, date, time]):
            messagebox.showerror(
                "Validation Error",
                "Please complete all appointment fields."
            )
            return

        # Validate date
        try:
            selected_date = datetime.strptime(
                date,
                "%Y-%m-%d"
            ).date()

            if selected_date < datetime.now().date():
                messagebox.showerror(
                    "Validation Error",
                    "Appointment date cannot be in the past."
                )
                return

        except ValueError:
            messagebox.showerror(
                "Validation Error",
                "Please use the date format YYYY-MM-DD."
            )
            return

        # Check duplicate appointment
        for appointment in appointments:

            if (
                appointment["doctor"] == doctor
                and appointment["date"] == date
                and appointment["time"] == time
            ):

                messagebox.showerror(
                    "Time Slot Unavailable",
                    "This doctor already has an appointment at this time."
                )

                return

        # Confirmation dialog
        confirmation = messagebox.askyesno(
            "Confirm Appointment",
            f"Patient: {patient}\n"
            f"Doctor: {doctor}\n"
            f"Date: {date}\n"
            f"Time: {time}\n\n"
            "Do you want to confirm this appointment?"
        )

        if not confirmation:
            return

        appointment = {
            "patient": patient,
            "doctor": doctor,
            "date": date,
            "time": time
        }

        appointments.append(appointment)

        messagebox.showinfo(
            "Appointment Confirmed",
            "The appointment has been booked successfully."
        )

        patient_var.set("")
        doctor_var.set("")
        date_var.set("")
        time_var.set("")

    button = create_button(
        content_frame,
        "Book Appointment",
        book_appointment
    )

    button.pack(
        padx=40,
        pady=10,
        anchor="w"
    )


# ============================================================
# DOCTOR DASHBOARD
# ============================================================

def show_doctor_dashboard():

    clear_content()

    create_title(
        content_frame,
        "Doctor Dashboard",
        "View appointments, patient records, diagnosis and prescriptions"
    )

    notebook = ttk.Notebook(content_frame)

    notebook.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=10
    )

    # ========================================================
    # TODAY'S APPOINTMENTS
    # ========================================================

    appointments_tab = tk.Frame(
        notebook,
        bg=WHITE
    )

    notebook.add(
        appointments_tab,
        text="Today's Appointments"
    )

    columns = (
        "patient",
        "doctor",
        "date",
        "time"
    )

    appointment_tree = ttk.Treeview(
        appointments_tab,
        columns=columns,
        show="headings"
    )

    appointment_tree.heading(
        "patient",
        text="Patient"
    )

    appointment_tree.heading(
        "doctor",
        text="Doctor"
    )

    appointment_tree.heading(
        "date",
        text="Date"
    )

    appointment_tree.heading(
        "time",
        text="Time"
    )

    appointment_tree.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    today = datetime.now().strftime("%Y-%m-%d")

    for appointment in appointments:

        if appointment["date"] == today:

            appointment_tree.insert(
                "",
                "end",
                values=(
                    appointment["patient"],
                    appointment["doctor"],
                    appointment["date"],
                    appointment["time"]
                )
            )

    # ========================================================
    # PATIENT RECORDS
    # ========================================================

    records_tab = tk.Frame(
        notebook,
        bg=WHITE
    )

    notebook.add(
        records_tab,
        text="Patient Records"
    )

    record_columns = (
        "id",
        "name",
        "age",
        "gender",
        "phone",
        "address"
    )

    record_tree = ttk.Treeview(
        records_tab,
        columns=record_columns,
        show="headings"
    )

    for column in record_columns:

        record_tree.heading(
            column,
            text=column.title()
        )

    record_tree.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    for patient in patients:

        record_tree.insert(
            "",
            "end",
            values=(
                patient["id"],
                patient["name"],
                patient["age"],
                patient["gender"],
                patient["phone"],
                patient["address"]
            )
        )

    # ========================================================
    # DIAGNOSIS AND PRESCRIPTION
    # ========================================================

    medical_tab = tk.Frame(
        notebook,
        bg=WHITE
    )

    notebook.add(
        medical_tab,
        text="Diagnosis & Prescription"
    )

    tk.Label(
        medical_tab,
        text="Select Patient:",
        font=("Arial", 11, "bold"),
        bg=WHITE
    ).pack(
        anchor="w",
        padx=30,
        pady=(30, 5)
    )

    medical_patient_var = tk.StringVar()

    medical_patient_combo = ttk.Combobox(
        medical_tab,
        textvariable=medical_patient_var,
        values=[
            f"{p['id']} - {p['name']}"
            for p in patients
        ],
        state="readonly",
        width=50
    )

    medical_patient_combo.pack(
        anchor="w",
        padx=30
    )

    tk.Label(
        medical_tab,
        text="Diagnosis:",
        font=("Arial", 11, "bold"),
        bg=WHITE
    ).pack(
        anchor="w",
        padx=30,
        pady=(20, 5)
    )

    diagnosis_text = tk.Text(
        medical_tab,
        height=5,
        width=70
    )

    diagnosis_text.pack(
        padx=30
    )

    tk.Label(
        medical_tab,
        text="Prescription:",
        font=("Arial", 11, "bold"),
        bg=WHITE
    ).pack(
        anchor="w",
        padx=30,
        pady=(20, 5)
    )

    prescription_text = tk.Text(
        medical_tab,
        height=5,
        width=70
    )

    prescription_text.pack(
        padx=30
    )

    def save_medical_record():

        if not medical_patient_var.get():
            messagebox.showerror(
                "Error",
                "Please select a patient."
            )
            return

        diagnosis = diagnosis_text.get(
            "1.0",
            tk.END
        ).strip()

        prescription = prescription_text.get(
            "1.0",
            tk.END
        ).strip()

        if not diagnosis:
            messagebox.showerror(
                "Error",
                "Please enter the diagnosis."
            )
            return

        if not prescription:
            messagebox.showerror(
                "Error",
                "Please enter the prescription."
            )
            return

        messagebox.showinfo(
            "Saved",
            "Diagnosis and prescription saved successfully."
        )

        diagnosis_text.delete(
            "1.0",
            tk.END
        )

        prescription_text.delete(
            "1.0",
            tk.END
        )

    create_button(
        medical_tab,
        "Save Medical Record",
        save_medical_record
    ).pack(
        anchor="w",
        padx=30,
        pady=20
    )

    # ========================================================
    # LAB RESULTS
    # ========================================================

    lab_tab = tk.Frame(
        notebook,
        bg=WHITE
    )

    notebook.add(
        lab_tab,
        text="Lab Results"
    )

    tk.Label(
        lab_tab,
        text="Laboratory Results",
        font=("Arial", 18, "bold"),
        bg=WHITE,
        fg=DARK
    ).pack(
        anchor="w",
        padx=30,
        pady=30
    )

    lab_columns = (
        "patient",
        "test",
        "result"
    )

    lab_tree = ttk.Treeview(
        lab_tab,
        columns=lab_columns,
        show="headings"
    )

    lab_tree.heading(
        "patient",
        text="Patient"
    )

    lab_tree.heading(
        "test",
        text="Test"
    )

    lab_tree.heading(
        "result",
        text="Result"
    )

    lab_tree.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=10
    )

    # Sample laboratory data
    lab_tree.insert(
        "",
        "end",
        values=(
            "Example Patient",
            "Blood Test",
            "Normal"
        )
    )


# ============================================================
# BILLING
# ============================================================

def show_billing():

    clear_content()

    create_title(
        content_frame,
        "Billing Section",
        "Create and review patient bills"
    )

    form = tk.Frame(
        content_frame,
        bg=WHITE
    )

    form.pack(
        padx=40,
        pady=20,
        anchor="w"
    )

    patient_var = tk.StringVar()
    service_var = tk.StringVar()
    amount_var = tk.StringVar()

    tk.Label(
        form,
        text="Patient:",
        font=("Arial", 11, "bold"),
        bg=WHITE
    ).grid(
        row=0,
        column=0,
        sticky="w",
        pady=10
    )

    patient_combo = ttk.Combobox(
        form,
        textvariable=patient_var,
        values=[
            f"{p['id']} - {p['name']}"
            for p in patients
        ],
        state="readonly",
        width=40
    )

    patient_combo.grid(
        row=0,
        column=1,
        padx=20
    )

    tk.Label(
        form,
        text="Service:",
        font=("Arial", 11, "bold"),
        bg=WHITE
    ).grid(
        row=1,
        column=0,
        sticky="w",
        pady=10
    )

    service_entry = tk.Entry(
        form,
        textvariable=service_var,
        width=43
    )

    service_entry.grid(
        row=1,
        column=1,
        padx=20
    )

    tk.Label(
        form,
        text="Amount (RWF):",
        font=("Arial", 11, "bold"),
        bg=WHITE
    ).grid(
        row=2,
        column=0,
        sticky="w",
        pady=10
    )

    amount_entry = tk.Entry(
        form,
        textvariable=amount_var,
        width=43
    )

    amount_entry.grid(
        row=2,
        column=1,
        padx=20
    )

    bill_tree = ttk.Treeview(
        content_frame,
        columns=(
            "patient",
            "service",
            "amount"
        ),
        show="headings"
    )

    bill_tree.heading(
        "patient",
        text="Patient"
    )

    bill_tree.heading(
        "service",
        text="Service"
    )

    bill_tree.heading(
        "amount",
        text="Amount (RWF)"
    )

    bill_tree.pack(
        fill="both",
        expand=True,
        padx=40,
        pady=20
    )

    def add_bill():

        patient = patient_var.get().strip()
        service = service_var.get().strip()
        amount = amount_var.get().strip()

        if not patient or not service or not amount:

            messagebox.showerror(
                "Validation Error",
                "Please complete all billing fields."
            )

            return

        try:
            amount_number = float(amount)

            if amount_number <= 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Validation Error",
                "Amount must be a positive number."
            )

            return

        bill_tree.insert(
            "",
            "end",
            values=(
                patient,
                service,
                f"{amount_number:,.0f}"
            )
        )

        messagebox.showinfo(
            "Billing",
            "Bill added successfully."
        )

        patient_var.set("")
        service_var.set("")
        amount_var.set("")

    create_button(
        content_frame,
        "Add Bill",
        add_bill
    ).pack(
        padx=40,
        pady=5,
        anchor="w"
    )


# ============================================================
# LOGIN WINDOW
# ============================================================

def login():

    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:

        messagebox.showerror(
            "Login Error",
            "Please enter username and password."
        )

        return

    if username == "admin" and password == "1234":

        login_window.destroy()

        root.deiconify()

        show_home()

    else:

        messagebox.showerror(
            "Login Error",
            "Invalid username or password."
        )


# ============================================================
# MAIN INTERFACE
# ============================================================

root.withdraw()

main_container = tk.Frame(
    root,
    bg=WHITE
)

main_container.pack(
    fill="both",
    expand=True
)


# ============================================================
# SIDEBAR
# ============================================================

sidebar = tk.Frame(
    main_container,
    bg=SECONDARY,
    width=230
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


tk.Label(
    sidebar,
    text="HOSPITAL\nSYSTEM",
    font=("Arial", 20, "bold"),
    bg=SECONDARY,
    fg=WHITE,
    justify="center"
).pack(
    pady=(30, 40)
)


def sidebar_button(text, command):

    button = tk.Button(
        sidebar,
        text=text,
        command=command,
        font=("Arial", 11, "bold"),
        bg=SECONDARY,
        fg=WHITE,
        activebackground=PRIMARY,
        activeforeground=WHITE,
        relief="flat",
        anchor="w",
        padx=25,
        pady=12,
        cursor="hand2"
    )

    button.pack(
        fill="x",
        pady=2
    )


sidebar_button(
    "🏠  Dashboard",
    show_home
)

sidebar_button(
    "👤  Register Patient",
    show_patient_registration
)

sidebar_button(
    "📅  Book Appointment",
    show_appointment_booking
)

sidebar_button(
    "🩺  Doctor Dashboard",
    show_doctor_dashboard
)

sidebar_button(
    "💳  Billing",
    show_billing
)


# ============================================================
# CONTENT AREA
# ============================================================

content_frame = tk.Frame(
    main_container,
    bg=WHITE
)

content_frame.pack(
    side="right",
    fill="both",
    expand=True
)


# ============================================================
# LOGIN WINDOW
# ============================================================

login_window = tk.Toplevel()

login_window.title(
    "Hospital Management System - Login"
)

login_window.geometry(
    "500x450"
)

login_window.resizable(
    False,
    False
)

login_window.configure(
    bg=LIGHT
)


tk.Label(
    login_window,
    text="Hospital Management System",
    font=("Arial", 22, "bold"),
    bg=LIGHT,
    fg=SECONDARY
).pack(
    pady=(50, 10)
)


tk.Label(
    login_window,
    text="Login",
    font=("Arial", 16, "bold"),
    bg=LIGHT,
    fg=DARK
).pack(
    pady=10
)


tk.Label(
    login_window,
    text="Username",
    font=("Arial", 11, "bold"),
    bg=LIGHT
).pack(
    pady=(15, 5)
)


username_entry = tk.Entry(
    login_window,
    font=("Arial", 12),
    width=30
)

username_entry.pack()


tk.Label(
    login_window,
    text="Password",
    font=("Arial", 11, "bold"),
    bg=LIGHT
).pack(
    pady=(15, 5)
)


password_entry = tk.Entry(
    login_window,
    font=("Arial", 12),
    width=30,
    show="*"
)

password_entry.pack()


tk.Button(
    login_window,
    text="Login",
    command=login,
    font=("Arial", 11, "bold"),
    bg=PRIMARY,
    fg=WHITE,
    activebackground=SECONDARY,
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    padx=30,
    pady=10
).pack(
    pady=25
)


tk.Label(
    login_window,
    text="Demo Login\nUsername: admin\nPassword: 1234",
    font=("Arial", 10),
    bg=LIGHT,
    fg="#607d8b"
).pack(
    pady=5
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()