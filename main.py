from saving_project import interest
from saving_project import display

def main():
    print("=== Program Kalkulator Bunga Tabungan ===")
    
    principal = float(input("Masukkan saldo awal (contoh: 80000): "))
    rate = float(input("Masukkan bunga tahunan (misal 5% -> 0.05): "))
    years = int(input("Masukkan lama menabung (tahun): "))
    print() 
    
    ci = interest.compound_interest(principal, rate, years)
    si = interest.simple_interest(principal, rate, years)
    
    display.print_result(principal, rate, years, ci, si)

if __name__ == "__main__":
    main()