import math
import random


def create_petal(cx, cy, radius, rotation, points=80):

    path = []

    for i in range(points + 1):

        theta = math.pi * i / points

        r = radius * math.sin(theta)

        x = r * math.cos(theta)
        y = r * math.sin(theta)

        angle = math.radians(rotation)

        rotated_x = (
            x * math.cos(angle)
            - y * math.sin(angle)
        )

        rotated_y = (
            x * math.sin(angle)
            + y * math.cos(angle)
        )

        final_x = cx + rotated_x
        final_y = cy + rotated_y

        if i == 0:
            path.append(
                f"M {final_x:.2f} {final_y:.2f}"
            )
        else:
            path.append(
                f"L {final_x:.2f} {final_y:.2f}"
            )

    return " ".join(path)


def create_flower(
    petals=36,
    radius=230,
    variation=0
):

    paths = []

    angle_step = 360 / petals

    random.seed(variation)

    for petal in range(petals):

        rotation = petal * angle_step

        petal_radius = radius + random.randint(-12, 12)

        path = create_petal(
            300,
            300,
            petal_radius,
            rotation
        )

        paths.append(path)

    return paths


def flower_svg(
    petals=36,
    radius=230,
    variation=0
):

    paths = create_flower(
        petals,
        radius,
        variation
    )

    svg_paths = ""

    for index, path in enumerate(paths):

        delay = index * 0.08

        svg_paths += f"""
        <path
            d="{path}"
            class="petal"
            style="animation-delay:{delay}s"
        />
        """

    return f"""
    <svg
        width="600"
        height="600"
        viewBox="0 0 600 600"
        xmlns="http://www.w3.org/2000/svg"
    >

        <rect
            width="600"
            height="600"
            rx="25"
            fill="#0A0F0D"
        />

        {svg_paths}

        <circle
            cx="300"
            cy="300"
            r="18"
            fill="#39FF85"
        />

        <style>

            .petal {{
                fill: none;
                stroke: #39FF85;
                stroke-width: 1.8;
                opacity: 0;

                stroke-dasharray: 1000;
                stroke-dashoffset: 1000;

                animation:
                    drawPetal 1.8s ease forwards;
            }}

            @keyframes drawPetal {{

                from {{
                    opacity: 0;
                    stroke-dashoffset: 1000;
                }}

                to {{
                    opacity: 0.8;
                    stroke-dashoffset: 0;
                }}

            }}

        </style>

    </svg>
    """