from flask import Flask, redirect, url_for, abort

app = Flask(__name__)

# Data dummy untuk simulasi database produk HP
database_hp = {
    1: "Samsung Galaxy S24 Ultra",
    2: "iPhone 15 Pro Max",
    3: "Xiaomi 14",
    4: "Oppo Find X7",
    5: "Vivo X100 Pro"
}

# 1. Empat Route Statis (Halaman Project)
@app.route('/')
def beranda():
    return "<h1>Selamat datang di Toko HP Terpercaya!</h1><p>Temukan smartphone impianmu di sini.</p>"

@app.route('/tentang')
def tentang():
    return "<h1>Tentang Kami</h1><p>Kami adalah distributor resmi berbagai merk HP terkemuka sejak 2020.</p>"

@app.route('/layanan')
def layanan():
    return "<h1>Layanan</h1><p>Penjualan HP Baru, Servis Resmi, dan Tukar Tambah.</p>"

@app.route('/kontak')
def kontak():
    return "<h1>Kontak</h1><p>Hubungi CS kami di: support@tokohp.com</p>"


# 2 & 4. Dynamic Route (Cek & User) + Validasi + Redirect & URL_For
@app.route('/cek/<username>')
def cek_username(username):
    # Validasi: Username harus berupa huruf/angka (alphanumeric) dan minimal 4 karakter
    if username.isalnum() and len(username) >= 4:
        # Syarat 4: Menggunakan redirect dan url_for
        return redirect(url_for('profil_user', username=username))
    else:
        return "<b>Validasi Gagal:</b> Username tidak valid! Harus gabungan huruf/angka dan minimal 4 karakter."

@app.route('/user/<username>')
def profil_user(username):
    return f"<h1>Profil Member</h1><p>Selamat datang, <b>{username}</b>! Anda login sebagai pelanggan setia Toko HP.</p>"


# 3. Route Converter INT dan Abort(404)
@app.route('/produk/<int:id>')
def detail_produk(id):
    # Mengecek apakah ID produk ada di dalam database_hp
    if id not in database_hp:
        # Syarat 3: Memanggil abort(404) jika data tidak ditemukan
        abort(404)
    
    merk_hp = database_hp[id]
    return f"<h1>Detail Produk</h1><p>Anda sedang melihat produk: <b>{merk_hp}</b></p>"


# 5. Custom Halaman Error 404
@app.errorhandler(404)
def halaman_tidak_ditemukan(e):
    # Syarat 5: Membuat custom halaman error 404
    return "<h1>404 - Halaman Tidak Ditemukan</h1><p>Maaf, produk HP atau halaman yang Anda cari tidak ada di sistem kami.</p>", 404

if __name__ == '__main__':
    app.run(debug=True)