import streamlit as st
import random
import matplotlib.pyplot as plt

st.title("Supermarket Checkout Queue Simulation")

# Inputs
st.sidebar.header("Input Parameters")
customers = st.sidebar.slider("Number of Customers", 10, 100, 30)
cashiers = st.sidebar.slider("Number of Cashiers", 1, 5, 2)
service_time = st.sidebar.slider("Service Time", 1, 5, 2)

# Simulation function
def simulate(customers, cashiers, service_time):
    queue = 0
    waiting_times = []
    
    for i in range(customers):
        queue += 1
        served = min(queue, cashiers)
        queue -= served
        
        wait = queue * service_time
        waiting_times.append(wait)
    
    avg_wait = sum(waiting_times) / len(waiting_times)
    return waiting_times, avg_wait

# Run Simulation
waiting_times, avg_wait = simulate(customers, cashiers, service_time)

st.write("### Average Waiting Time:", avg_wait)

# ---------------- GRAPH 1 ----------------
st.subheader("Graph 1: Customers vs Waiting Time")

customers_list = [10, 20, 30, 40, 50]
wait_results = []

for c in customers_list:
    _, avg = simulate(c, 1, service_time)
    wait_results.append(avg)

fig1 = plt.figure()
plt.plot(customers_list, wait_results, marker='o')
plt.xlabel("Customers")
plt.ylabel("Waiting Time")
plt.title("Customers vs Waiting Time")
st.pyplot(fig1)

# ---------------- GRAPH 2 ----------------
st.subheader("Graph 2: Cashiers vs Waiting Time")

cashiers_list = [1, 2, 3, 4, 5]
wait_results2 = []

for c in cashiers_list:
    _, avg = simulate(customers, c, service_time)
    wait_results2.append(avg)

fig2 = plt.figure()
plt.plot(cashiers_list, wait_results2, marker='o')
plt.xlabel("Cashiers")
plt.ylabel("Waiting Time")
plt.title("Cashiers vs Waiting Time")
st.pyplot(fig2)

# ---------------- GRAPH 3 ----------------
st.subheader("Graph 3: Queue Trend Over Time")

fig3 = plt.figure()
plt.plot(range(len(waiting_times)), waiting_times, marker='o')
plt.xlabel("Customer Number")
plt.ylabel("Waiting Time")
plt.title("Queue Trend")
st.pyplot(fig3)