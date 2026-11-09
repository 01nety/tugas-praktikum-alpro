def print_result(principal, rate, years, ci, si):
    """Menampilkan display Saldo Awal, Bunga Tahunan, Lama Menabung, dan Nilai Akhir (Majemuk & Sederhana)"""
    print("===== HASIL PERHITUNGAN TABUNGAN =====")
    print(f"Saldo Awal      : ¥{principal:,.1f}")
    print(f"Bunga Tahunan   : {rate * 100:.1f}%")
    print(f"Lama Menabung   : {years} tahun")
    print("-" * 45)
    print(f"Nilai Akhir (Bunga Majemuk)    : ¥{ci:,.2f}")
    print(f"Nilai Akhir (Bunga Sederhana)  : ¥{si:,.2f}")
    print("=" * 45)