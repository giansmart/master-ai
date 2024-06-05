import numpy as np

def pregunta_1(file_name):
    with open(file_name,"r") as file:
        lines = file.readlines()
        for line in lines:
            if line == "-1":
                break
            numeros_arr = [ int(num) for num in line.split(" ")]
            j = numeros_arr[-1]
            i = numeros_arr[-2]
            suma = sum(numeros_arr[i:j + 1])
            print(f"The sum of elements from index {i} to {j} is {suma}.")

#pregunta_1("sequences.in")

def pregunta_2(file_name):
    with open(file_name,"r") as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if line == "END":
                break
            print(f"Prase {index + 1}")
            phrase = line.split(" ")
            word_dict = {}
            for word in phrase:
                word = word.replace("\n","")
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1 

            sorted_word_dict = dict(sorted(word_dict.items()))
            for word in sorted_word_dict:
                times = "times" if sorted_word_dict[word] > 1 else "time"
                print(f"The word '{word}' appears {sorted_word_dict[word]} {times}")

#pregunta_2("words.in")

def pregunta_3(file_name):
    with open(file_name,"r") as file:
        lines = file.readlines()
        for line in lines:
            if line == "-1":
                break
            temperatures = [ float(num) for num in line.split(" ")]
            end = int(temperatures[-1])
            start = int(temperatures[-2])
            avg = round(np.average(temperatures[start:end + 1]),2)
            print(f"The average temperature from day {start} to {end} is {format(avg,'.2f')}.")

#pregunta_3("temperatures.in")

def pregunta_4(file_name):
    with open(file_name,"r") as file:
        lines = file.readlines()
        for line in lines:
            if line == "-1":
                break
            sales = [ float(num) for num in line.split(" ")]
            threshold = sales[-1]

            highest_sales_day = np.argmax(sales)
            lowest_sales_day = np.argmin(sales)
            counting_sales = sales[:len(sales) - 1]
            total_sales = round(np.sum(counting_sales),2)
            days_above_threshold = np.argwhere(np.array(counting_sales) > threshold).flatten().tolist()

            print(f"Highest sales on day {highest_sales_day}")
            print(f"Lowest sales on day {lowest_sales_day}")
            print(f"Total sales: {total_sales}")
            print(f"Days with sales above threshold: {days_above_threshold}")

            print()

pregunta_4("sales.in")