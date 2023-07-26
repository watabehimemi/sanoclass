import random 
import matplotlib.pyplot as plt


def estimate_pi(num_samples): 

    num_points_inside_circle = 0 

    num_points_total = 0 

    points_inside_circle_x = [] 

    points_inside_circle_y = [] 

    points_outside_circle_x = [] 

    points_outside_circle_y = [] 

    for _ in range(num_samples): 

        x = random.uniform(-1, 1) 

        y = random.uniform(-1, 1) 

        distance = x**2 + y**2 

        if distance <= 1: 

            num_points_inside_circle += 1 

            points_inside_circle_x.append(x) 

            points_inside_circle_y.append(y) 

        else: 

            points_outside_circle_x.append(x) 

            points_outside_circle_y.append(y) 

        num_points_total += 1 

        pi_estimate = 4 * (num_points_inside_circle / num_points_total) 

    return ( 

        pi_estimate, 

        points_inside_circle_x, 

        points_inside_circle_y, 

        points_outside_circle_x, 

        points_outside_circle_y, 

    ) 

 

# サンプル数を指定して円周率を推定 

num_samples = 1000 

pi, inside_x, inside_y, outside_x, outside_y = estimate_pi(num_samples) 

# グラフの描画 

fig, ax = plt.subplots() 

# 正方形を描画 

square = plt.Rectangle((-1, -1), 2, 2, linewidth=1, edgecolor="black", facecolor="none") 

ax.add_patch(square) 

# 円を描画 

circle = plt.Circle((0, 0), 1, linewidth=1, edgecolor="black", facecolor="none") 

ax.add_patch(circle) 

# 点をプロット 

ax.scatter(inside_x, inside_y, color="blue", label="Inside Circle") 

ax.scatter(outside_x, outside_y, color="red", label="Outside Circle") 

ax.set_aspect("equal", adjustable="box") 

ax.set_xlim([-1.5, 1.5]) 

ax.set_ylim([-1.5, 1.5]) 

ax.legend() 

plt.title(f"Estimation of Pi: {pi}") 

plt.show() 