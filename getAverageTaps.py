
times = [1.546, 0.262, 1.567, 0.178, 1.178, 0.142, 0.857, 0.192, 0.887, 0.230, 0.946, 0.213, 0.884, 0.249, 1.118, 0.237, 1.304, 0.232, 1.257, 0.201, 1.461, 0.162, 0.942, 0.226, 0.709, 0.270, 1.097, 0.227, 1.235, 0.218, 1.430, 0.209, 1.500, 0.189, 1.187, 0.190, 1.197, 0.211, 1.022, 0.198, 1.301, 0.229, 0.962, 0.271, 0.793, 0.343, 1.593, 0.293, 1.321, 0.361, 1.379, 0.330, 1.655, 0.357, 1.299, 0.629]

# times.sort()
# print(times)
# print(times)


# print(len(times))
diferencias = []
for i in range(len(times)-1, -1, -2):
    time_1 = times[i] 
    time_2 = times[i-1] 
    
    diferencia = time_2 - time_1
    diferencias.append(diferencia)

print(min(diferencias))
print(max(diferencias))
average = sum(diferencias)/len(diferencias)

print(average)