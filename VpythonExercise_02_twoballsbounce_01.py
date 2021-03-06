import vpython as vp

initial_position_1 = vp.vector(-10, 12, 1)
initial_velocity_1 = vp.vector(10, -12, -2)
ball_1 = vp.sphere(pos=initial_position_1, radius=0.5, color=vp.color.cyan, make_trail=True)

initial_position_2 = vp.vector(-10, -5, -1)
initial_velocity_2 = vp.vector(14, 5, 2)
ball_2 = vp.sphere(pos=initial_position_2, radius=0.5, color=vp.color.yellow, make_trail=True)

wall_center = vp.vector(0., 0., 0.)
wall_dimensions = vp.vector(0.25, 10., 10.)
wall = vp.box(pos=wall_center, size=wall_dimensions, color=vp.color.magenta)

animation_time_step = 0.01  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.005
stop_time = 2

time = 0.
ball_velocity_1 = initial_velocity_1
ball_velocity_2 = initial_velocity_2
while time < stop_time:
    vp.rate(rate_of_animation)
    if ball_1.pos.x > wall.pos.x - 0.30:
        ball_velocity_1.x = -ball_velocity_1.x  # reverse ball_1 velocity
    if ball_2.pos.x > wall.pos.x - 0.30:
        ball_velocity_2.x = -ball_velocity_2.x  # reverse ball_2 velocity

    ball_1.pos.x += ball_velocity_1.x * time_step
    ball_1.pos.y += ball_velocity_1.y * time_step
    ball_1.pos.z += ball_velocity_1.z * time_step

    ball_2.pos.x += ball_velocity_2.x * time_step
    ball_2.pos.y += ball_velocity_2.y * time_step
    ball_2.pos.z += ball_velocity_2.z * time_step

    time += time_step
