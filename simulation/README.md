# MORSE Simulation

## Installation

1. [Install MORSE simulation environment][morse-install].

    ```
    $ sudo apt-get install morse-simulator
    $ morse check
    ```

    `morse check` should pass with no errors.

2. Install dependencies for robot controller:

    ```
    $ pip3 install -r requirements.txt
    ```

3. Import simulation.

   ```
   $ morse import . thermalcomfort
   ```

4. Start simulation.

    ```
    $ morse run thermalcomfort
    ```

5. Start robot controller in a separate terminal.

    ```
    $ python3 scripts/cli.py
    ```

[morse-install]: https://www.openrobots.org/morse/doc/stable/user/installation.html
