# MORSE Simulation

## Installation

1. [Install MORSE simulation environment][morse-install].

    ```
    $ sudo apt-get install morse-simulator
    $ morse check
    ```

2. Install dependencies for robot controller:

    ```
    $ pip3 install -r requirements.txt
    ```

3. Start simulation.

    ```
    $ morse run sim.py
    ```

4. Start robot controller in a separate terminal.

    ```
    $ python3 cli.py
    ```

[morse-install]: https://www.openrobots.org/morse/doc/stable/user/installation.html
