def math_operations(*args, **kwargs):
    operations = ""
    steps = 0
    for number in args:
        steps += 1
        if steps == 1:
            kwargs["a"] += number
        elif steps == 2:
            kwargs["s"] -= number
        elif steps == 3:
            if number != 0:
                kwargs["d"] /= number
        elif steps == 4:
            kwargs["m"] *= number
            steps = 0

    sorted_data = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sorted_data:
        operations += f"{key}: {value:.1f}" + "\n"

    return operations
  
