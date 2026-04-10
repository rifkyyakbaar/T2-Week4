# NIM   : F1D02310149
# Kelas : D

import sys
import re
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QStackedWidget,
                               QDateEdit, QRadioButton, QButtonGroup,
                               QTextEdit, QMessageBox, QFrame, QGridLayout, QSizePolicy)
from PySide6.QtCore import Qt, Signal, QObject, QDate

class PengelolaSinyal(QObject):
    step_berubah = Signal(int)

class FormMultiStep(QWidget):
    def __init__(self):
        super().__init__()
        self.sinyal = PengelolaSinyal()
        self.setup_ui()
        self.setup_signals()
        self.update_tampilan_step(0) 

    def setup_ui(self):
        self.setWindowTitle("Form Registrasi")
        self.resize(550, 550)
        self.setStyleSheet("""
            QWidget { background-color: #F8F9FA; font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; color: #333; }
            QLineEdit, QDateEdit, QTextEdit { 
                padding: 8px; border-radius: 4px; border: 1px solid #bdc3c7; background-color: white; 
            }
            QPushButton { padding: 8px 15px; border-radius: 4px; font-weight: bold; border: none; }
            QPushButton#btn_lanjut { background-color: #3498db; color: white; }
            QPushButton#btn_lanjut:disabled { background-color: #95a5a6; color: white; }
            QPushButton#btn_kembali { background-color: #f1f2f6; color: #2c3e50; border: 1px solid #bdc3c7; }
        """)

        layout_utama = QVBoxLayout(self)
        layout_utama.setContentsMargins(20, 20, 20, 20)

        layout_indikator = QGridLayout()
        layout_indikator.setContentsMargins(10, 0, 10, 0)
        
        self.step1_bulat = QLabel("1")
        self.step1_teks = QLabel("Data Pribadi")
        
        self.garis1 = QFrame()
        self.garis1.setFrameShape(QFrame.HLine)
        self.garis1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.step2_bulat = QLabel("2")
        self.step2_teks = QLabel("Kontak")
        
        self.garis2 = QFrame()
        self.garis2.setFrameShape(QFrame.HLine)
        self.garis2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.step3_bulat = QLabel("3")
        self.step3_teks = QLabel("Akun")

        for label in [self.step1_bulat, self.step2_bulat, self.step3_bulat]:
            label.setAlignment(Qt.AlignCenter)
            label.setFixedSize(35, 35)

        for teks in [self.step1_teks, self.step2_teks, self.step3_teks]:
            teks.setAlignment(Qt.AlignCenter)

        layout_indikator.addWidget(self.step1_bulat, 0, 0, alignment=Qt.AlignCenter)
        layout_indikator.addWidget(self.garis1, 0, 1, alignment=Qt.AlignVCenter)
        layout_indikator.addWidget(self.step2_bulat, 0, 2, alignment=Qt.AlignCenter)
        layout_indikator.addWidget(self.garis2, 0, 3, alignment=Qt.AlignVCenter)
        layout_indikator.addWidget(self.step3_bulat, 0, 4, alignment=Qt.AlignCenter)

        layout_indikator.addWidget(self.step1_teks, 1, 0, alignment=Qt.AlignTop | Qt.AlignHCenter)
        layout_indikator.addWidget(self.step2_teks, 1, 2, alignment=Qt.AlignTop | Qt.AlignHCenter)
        layout_indikator.addWidget(self.step3_teks, 1, 4, alignment=Qt.AlignTop | Qt.AlignHCenter)

        layout_utama.addLayout(layout_indikator)
        layout_utama.addSpacing(25)

        self.label_judul = QLabel("<b>Step 1: Data Pribadi</b>")
        self.label_judul.setStyleSheet("font-size: 18px; color: #2c3e50; margin-bottom: 10px;")
        layout_utama.addWidget(self.label_judul)

        self.tumpukan_halaman = QStackedWidget()
        layout_utama.addWidget(self.tumpukan_halaman)

        self.buat_step1_pribadi()
        self.buat_step2_kontak()
        self.buat_step3_akun()

        layout_tombol = QHBoxLayout()
        self.btn_kembali = QPushButton("← Kembali")
        self.btn_kembali.setObjectName("btn_kembali")
        
        self.btn_lanjut = QPushButton("Lanjut →")
        self.btn_lanjut.setObjectName("btn_lanjut")

        layout_tombol.addWidget(self.btn_kembali)
        layout_tombol.addStretch()
        layout_tombol.addWidget(self.btn_lanjut)
        layout_utama.addLayout(layout_tombol)
        
        layout_utama.addSpacing(10)
        
        self.label_status = QLabel("Step 1 dari 3 — Lengkapi semua field untuk melanjutkan")
        self.label_status.setStyleSheet("color: #7f8c8d; font-size: 11px;")
        layout_utama.addWidget(self.label_status)

    def buat_step1_pribadi(self):
        halaman = QWidget()
        layout = QVBoxLayout(halaman)

        layout.addWidget(QLabel("Nama Lengkap"))
        self.input_nama = QLineEdit()
        layout.addWidget(self.input_nama)

        layout.addWidget(QLabel("Tanggal Lahir"))
        self.input_tgl = QDateEdit()
        self.input_tgl.setCalendarPopup(True)
        self.input_tgl.setDate(QDate.currentDate())
        layout.addWidget(self.input_tgl)

        layout.addWidget(QLabel("Jenis Kelamin"))
        layout_jk = QHBoxLayout()
        self.radio_l = QRadioButton("Laki-laki")
        self.radio_p = QRadioButton("Perempuan")
        self.grup_jk = QButtonGroup()
        self.grup_jk.addButton(self.radio_l)
        self.grup_jk.addButton(self.radio_p)
        layout_jk.addWidget(self.radio_l)
        layout_jk.addWidget(self.radio_p)
        layout_jk.addStretch()
        layout.addLayout(layout_jk)

        layout.addStretch()
        self.tumpukan_halaman.addWidget(halaman)

    def buat_step2_kontak(self):
        halaman = QWidget()
        layout = QVBoxLayout(halaman)

        layout.addWidget(QLabel("Email"))
        self.input_email = QLineEdit()
        layout.addWidget(self.input_email)

        layout.addWidget(QLabel("Telepon"))
        self.input_telepon = QLineEdit()
        layout.addWidget(self.input_telepon)
        
        self.error_telepon = QLabel("⚠ Nomor minimal 10 digit")
        self.error_telepon.setStyleSheet("color: #e67e22; font-size: 11px;")
        self.error_telepon.hide()
        layout.addWidget(self.error_telepon)

        layout.addWidget(QLabel("Alamat"))
        self.input_alamat = QTextEdit()
        self.input_alamat.setMaximumHeight(60)
        layout.addWidget(self.input_alamat)

        layout.addStretch()
        self.tumpukan_halaman.addWidget(halaman)

    def buat_step3_akun(self):
        halaman = QWidget()
        layout = QVBoxLayout(halaman)

        layout.addWidget(QLabel("Username"))
        self.input_user = QLineEdit()
        layout.addWidget(self.input_user)

        layout.addWidget(QLabel("Password"))
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_pass)

        layout.addWidget(QLabel("Confirm Password"))
        self.input_konfirmasi = QLineEdit()
        self.input_konfirmasi.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_konfirmasi)
        
        self.error_pass = QLabel("⚠ Password tidak cocok")
        self.error_pass.setStyleSheet("color: #e67e22; font-size: 11px;")
        self.error_pass.hide()
        layout.addWidget(self.error_pass)

        layout.addStretch()
        self.tumpukan_halaman.addWidget(halaman)

    def setup_signals(self):
        self.btn_lanjut.clicked.connect(self.maju_step)
        self.btn_kembali.clicked.connect(self.mundur_step)
        self.sinyal.step_berubah.connect(self.update_tampilan_step)

        self.input_nama.textChanged.connect(self.validasi_step)
        self.grup_jk.buttonClicked.connect(self.validasi_step)
        self.input_email.textChanged.connect(self.validasi_step)
        self.input_telepon.textChanged.connect(self.validasi_step)
        self.input_alamat.textChanged.connect(self.validasi_step)
        self.input_user.textChanged.connect(self.validasi_step)
        self.input_pass.textChanged.connect(self.validasi_step)
        self.input_konfirmasi.textChanged.connect(self.validasi_step)

    def set_gaya_validasi(self, widget, valid, teks_kosong=False):
        if valid:
            widget.setStyleSheet("border: 2px solid #27ae60; background-color: white;") 
        elif teks_kosong:
            widget.setStyleSheet("border: 1px solid #bdc3c7; background-color: white;") 
        else:
            widget.setStyleSheet("border: 2px solid #f39c12; background-color: white;") 

    def validasi_step(self):
        indeks = self.tumpukan_halaman.currentIndex()
        semua_valid = False

        if indeks == 0:
            nama = self.input_nama.text().strip()
            nama_valid = len(nama) > 0
            self.set_gaya_validasi(self.input_nama, nama_valid, len(nama)==0)
            jk_valid = self.grup_jk.checkedButton() is not None
            semua_valid = nama_valid and jk_valid

        elif indeks == 1:
            email = self.input_email.text().strip()
            email_valid = bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))
            self.set_gaya_validasi(self.input_email, email_valid, len(email)==0)

            telp = self.input_telepon.text().strip()
            telp_valid = telp.isdigit() and len(telp) >= 10
            self.set_gaya_validasi(self.input_telepon, telp_valid, len(telp)==0)
            
            if not telp_valid and len(telp) > 0:
                self.error_telepon.show()
            else:
                self.error_telepon.hide()

            alamat_valid = len(self.input_alamat.toPlainText().strip()) > 0
            self.set_gaya_validasi(self.input_alamat, alamat_valid, len(self.input_alamat.toPlainText())==0)

            semua_valid = email_valid and telp_valid and alamat_valid

        elif indeks == 2:
            user_valid = len(self.input_user.text().strip()) >= 4
            self.set_gaya_validasi(self.input_user, user_valid, len(self.input_user.text())==0)

            pass_valid = len(self.input_pass.text()) >= 5
            self.set_gaya_validasi(self.input_pass, pass_valid, len(self.input_pass.text())==0)

            konf_teks = self.input_konfirmasi.text()
            konf_valid = (konf_teks == self.input_pass.text()) and pass_valid
            self.set_gaya_validasi(self.input_konfirmasi, konf_valid, len(konf_teks)==0)
            
            if not konf_valid and len(konf_teks) > 0:
                self.error_pass.show()
            else:
                self.error_pass.hide()

            semua_valid = user_valid and pass_valid and konf_valid

        self.btn_lanjut.setEnabled(semua_valid)

    def maju_step(self):
        indeks = self.tumpukan_halaman.currentIndex()
        if indeks == 2: 
            QMessageBox.information(self, "Sukses", "Data Registrasi Berhasil Disimpan!")
            self.close()
            return
        self.sinyal.step_berubah.emit(indeks + 1)

    def mundur_step(self):
        self.sinyal.step_berubah.emit(self.tumpukan_halaman.currentIndex() - 1)

    def update_tampilan_step(self, indeks):
        self.tumpukan_halaman.setCurrentIndex(indeks)
        self.validasi_step()

        self.label_status.setText(f"Step {indeks + 1} dari 3 — Lengkapi semua field untuk melanjutkan")

        gaya_selesai = "background-color: #27ae60; color: white; border-radius: 17px; font-weight: bold; font-size: 16px;"
        gaya_aktif = "background-color: #3498db; color: white; border-radius: 17px; font-weight: bold; font-size: 16px;"   
        gaya_belum = "background-color: #bdc3c7; color: white; border-radius: 17px; font-weight: bold; font-size: 16px;"  
        
        garis_selesai = "background-color: #27ae60; max-height: 4px;"
        garis_belum = "background-color: #bdc3c7; max-height: 4px;"

        self.step1_bulat.setStyleSheet(gaya_belum); self.step1_bulat.setText("1")
        self.step2_bulat.setStyleSheet(gaya_belum); self.step2_bulat.setText("2")
        self.step3_bulat.setStyleSheet(gaya_belum); self.step3_bulat.setText("3")
        self.step1_teks.setStyleSheet("font-size: 12px; color: #bdc3c7; padding-top: 5px;")
        self.step2_teks.setStyleSheet("font-size: 12px; color: #bdc3c7; padding-top: 5px;")
        self.step3_teks.setStyleSheet("font-size: 12px; color: #bdc3c7; padding-top: 5px;")
        self.garis1.setStyleSheet(garis_belum)
        self.garis2.setStyleSheet(garis_belum)

        if indeks == 0:
            self.label_judul.setText("<b>Step 1: Data Pribadi</b>")
            self.btn_kembali.hide()
            self.btn_lanjut.setText("Lanjut →")
            
            self.step1_bulat.setStyleSheet(gaya_aktif)
            self.step1_teks.setStyleSheet("font-size: 12px; color: #27ae60; font-weight: bold; padding-top: 5px;")
            
        elif indeks == 1:
            self.label_judul.setText("<b>Step 2: Informasi Kontak</b>")
            self.btn_kembali.show()
            self.btn_lanjut.setText("Lanjut →")
            
            self.step1_bulat.setStyleSheet(gaya_selesai); self.step1_bulat.setText("✔")
            self.garis1.setStyleSheet(garis_selesai)
            self.step1_teks.setStyleSheet("font-size: 12px; color: #27ae60; font-weight: bold; padding-top: 5px;")
            
            self.step2_bulat.setStyleSheet(gaya_aktif)
            self.step2_teks.setStyleSheet("font-size: 12px; color: #3498db; font-weight: bold; padding-top: 5px;")
            
        elif indeks == 2:
            self.label_judul.setText("<b>Step 3: Informasi Akun</b>")
            self.btn_kembali.show()
            self.btn_lanjut.setText("Submit Data")
            
            self.step1_bulat.setStyleSheet(gaya_selesai); self.step1_bulat.setText("✔")
            self.garis1.setStyleSheet(garis_selesai)
            self.step1_teks.setStyleSheet("font-size: 12px; color: #27ae60; font-weight: bold; padding-top: 5px;")
            
            self.step2_bulat.setStyleSheet(gaya_selesai); self.step2_bulat.setText("✔")
            self.garis2.setStyleSheet(garis_selesai)
            self.step2_teks.setStyleSheet("font-size: 12px; color: #27ae60; font-weight: bold; padding-top: 5px;")
            
            self.step3_bulat.setStyleSheet(gaya_aktif)
            self.step3_teks.setStyleSheet("font-size: 12px; color: #3498db; font-weight: bold; padding-top: 5px;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormMultiStep()
    window.show()
    sys.exit(app.exec())