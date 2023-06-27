# Antminer Monitor [![follow on twitter][twitter]](https://twitter.com/intent/follow?screen_name=AntminerMonitor)

Features:

- Add as many miners as you want
- Supports miners S9, S11, S17, S17 Pro, S17+, T9, T9+, T17
- Check their hashrate, temperatures, fan speed, chip condition, HW Error Rate, Uptime
- Log errors to file
- Display total hashrate grouped by Model
- Password protected login page

TODO:
- scan network and detect machines
- per subnet/models
- reports of underperforming machines (simple TH check)
- Deep analysis (check logs of every machines)
- hourly, daily, weekly, monthly logs and stats
- cost of operation and profits
- machines to replace (log faults, underperforming TH)
- simple batch machines configurator
- machine locator (flashing light)
- simple dashboard with graphs (5min our 1hr logs)
- Add support for newer machines (x19)
- support BraiinsOS
- Auto-select the model when adding miners

## Screenshot

![Alt text](/antminermonitor/static/images/screenshot_v0.5.0.png?raw=true "Screenshot v0.5.0")

### Requirements

- Antminer Monitor requires Python 3

## Fresh Installation

1. Install requirements (Mac users don't forget `sudo`)
2. create the empty database
3. create the admin user
```sh
pip3 install -r requirements.txt
python3 app.py create-db
```

Default creadentials are `username: admin` - `password: antminermonitor`. You can change the password from the settings menu.

## Run the app

(Mac users don't forget `sudo`)

```sh
python3 app.py run -h 0.0.0.0 -p 8000
```

Fire up a browser and point it to `http://localhost:8000` if you are running the app on the same machine.

You can set the host `(-h)` and port `(-p)` parameters in your .flaskenv file to avoid typing them when starting the app.

## Development vs. Production mode

AntminerMonitor runs by default in development mode, using Flask's development server. In development mode, this server provides an interactive debugger and will reload when code is changed.

To switch to production mode, edit `.flaskenv` and set `FLASK_ENV="production"`

## Run AntminerMonitor as a service (systemd) (rapsberrypi)

Edit `antminermonitor.service` and adjust it properly to your environment

As root, run the following:

```sh
# Copy file service file to systemd's system folder
cp antminermonitor.service /etc/systemd/system/
# reload the daemon to apply changes
systemctl daemon-reload
# That’s it. We can now start the service:
systemctl start antminermonitor
# And automatically get it to start on boot
systemctl enable antminermonitor
```