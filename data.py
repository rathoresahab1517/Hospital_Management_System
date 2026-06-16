flask import





def seed():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Admin
        admin = User(username='admin', email='admin@hospital.com', name='System Admin', phone='1234567890', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)

        # Doctor users
        doc_data = [
            ('drsmith', 'dr.smith@hospital.com', 'Dr. John Smith', '1111111111', 'Cardiology', 'LIC001', 'MD, DM Cardiology', 15, 150.0, 'Mon-Fri', '09:00', '17:00'),
            ('drjones', 'dr.jones@hospital.com', 'Dr. Sarah Jones', '2222222222', 'Pediatrics', 'LIC002', 'MD, DCH', 10, 120.0, 'Mon-Sat', '10:00', '16:00'),
            ('drlee', 'dr.lee@hospital.com', 'Dr. David Lee', '3333333333', 'Orthopedics', 'LIC003', 'MS, DNB Ortho', 12, 200.0, 'Tue-Sat', '08:00', '14:00'),
        ]
        doctors = []
        for uname, email, name, phone, spec, lic, qual, exp, fee, days, t_start, t_end in doc_data:
            u = User(username=uname, email=email, name=name, phone=phone, role='doctor')
            u.set_password('doctor123')
            db.session.add(u)
            db.session.flush()
            d = Doctor(user_id=u.id, specialization=spec, license_number=lic, qualification=qual,
                       experience_years=exp, consultation_fee=fee, available_days=days,
                       available_time_start=t_start, available_time_end=t_end)
            db.session.add(d)
            doctors.append(d)

        # Patient users
        pat_data = [
            ('patient', 'patient@example.com', 'John Doe', '4444444444', 'Male', 'O+', '1990-05-15'),
            ('janes', 'jane@example.com', 'Jane Smith', '5555555555', 'Female', 'A+', '1985-10-20'),
            ('bobw', 'bob@example.com', 'Bob Wilson', '6666666666', 'Male', 'B+', '1978-03-08'),
        ]
        patients = []
        for uname, email, name, phone, gender, bg, dob_str in pat_data:
            u = User(username=uname, email=email, name=name, phone=phone, role='patient')
            u.set_password('patient123')
            db.session.add(u)
            db.session.flush()
            p = Patient(user_id=u.id, gender=gender, blood_group=bg,
                        date_of_birth=datetime.strptime(dob_str, '%Y-%m-%d').date(),
                        address='123 Main St, City', emergency_contact='9999999999')
            db.session.add(p)
            patients.append(p)

        db.session.commit()

# Appointments

# Prescription for completed appointment

# Bills