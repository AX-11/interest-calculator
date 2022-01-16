import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


# Mathematical funciton to be plotted
# All currency is in eur
def calculate_cost(
    months_elapsed,
    car_price,
    down_payment,
    monthly_interest,
):
    return car_price * (monthly_interest / 100) * months_elapsed + down_payment


months_elapsed = np.linspace(0, 120, 1000)

# Init parameters for graph
init_car_price = 3000
init_monthly_installment = 5
init_down_payment = 200
init_num_months = 24
init_interest = 3

# Create plot
fig, ax = plt.subplots()
(line,) = plt.plot(
    months_elapsed,
    calculate_cost(
        months_elapsed, init_car_price, init_down_payment, init_monthly_installment
    ),
    lw=2,
)
ax.set_xlabel("Months elapsed")
ax.set_ylabel("Money payed")
(car_line,) = plt.plot(months_elapsed, months_elapsed * 0 + init_car_price)
monthly = ax.text(
    0.99,
    0.05,
    "Monthly payment : ###€",
    transform=ax.transAxes,
    ha="right",
    va="bottom",
)

# Make room for sliders
plt.subplots_adjust(bottom=0.65)

# installments
axinstallment = plt.axes([0.25, 0.1, 0.65, 0.03])
installment_slider = Slider(
    ax=axinstallment,
    label="Monthly installments (%)",
    valmin=0,
    valmax=20,
    valinit=init_monthly_installment,
)

# down payment slider
axdown = plt.axes([0.25, 0.2, 0.65, 0.03])
down_payment_slider = Slider(
    ax=axdown,
    label="Down payment (€)",
    valmin=0,
    valmax=5000,
    valinit=init_down_payment,
)

# car price slider
axcar = plt.axes([0.25, 0.3, 0.65, 0.03])
car_price_slider = Slider(
    ax=axcar, label="Car price (€)", valmin=0, valmax=10000, valinit=init_car_price
)

# time scale slider
axmonth = plt.axes([0.25, 0.4, 0.65, 0.03])
month_slider = Slider(
    ax=axmonth,
    label="Months",
    valmin=1,
    valmax=120,
    valinit=init_num_months,
    valstep=[i for i in range(0, 121)],
)

# interest slider
axinterest = plt.axes([0.25, 0.5, 0.65, 0.03])
interest_slider = Slider(
    ax=axinterest, label="Interest (%)", valmin=0, valmax=100, valinit=init_interest
)


# Called when slider value changes
def update(val):
    line.set_ydata(
        calculate_cost(
            months_elapsed,
            car_price_slider.val,
            down_payment_slider.val,
            installment_slider.val,
        )
    )
    car_line.set_ydata(car_price_slider.val)
    ax.set_ylim([0, car_price_slider.val * 1.1])
    ax.set_xlim([0, month_slider.val])
    fig.canvas.draw_idle()
    monthly.set_text(
        f"Monthly payment: {round((car_price_slider.val * (installment_slider.val / 100)) * (1 + interest_slider.val / 100), 2)}€"
    )


# Register update function
down_payment_slider.on_changed(update)
installment_slider.on_changed(update)
car_price_slider.on_changed(update)
month_slider.on_changed(update)
interest_slider.on_changed(update)


ax.set_ylim([0, init_car_price * 1.1])
plt.show()
