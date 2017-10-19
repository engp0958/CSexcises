def days_to_start(month,date,feb):    
    month_12=[31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    days=0
    i=month-1
    while i>=1:
        days=days + month_12[i-1]
        i=i-1
    return days + date

def days_to_end(month, date,feb):
    month_12=[31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days=0
    days_partial=month_12[month-1]-date+1
    i=month+1
    while i<=12:
        days=days + month_12[i-1]
        i=i+1
    return days + days_partial

print days_to_end(1,1,29)+days_to_start(2,28,29)-366

