def compound_interest(principal, rate, time):
    """Menghitung nilai akhir dengan bunga majemuk: Future value = principal * (1 + rate)**time"""
    return principal * ((1 + rate) ** time)

def simple_interest(principal, rate, time):
    """Menghitung nilai akhir dengan bunga sederhana: Future value = Principal * rate * time + Principal"""
    # Berdasarkan rumus pada modul: Future value = Principal * rate * time (atau total akhir = pokok + bunga)
    return principal + (principal * rate * time)