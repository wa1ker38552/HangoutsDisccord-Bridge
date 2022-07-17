# HangoutsDisccord-Bridge

A bridge that sends messages from Hangouts to Discord.

Since there are various problems with the Hangups module, I used the logging from Hangups to send messages to Discord.

**Setup:**

1. Install hangups `pip install hangups`
2. Login using `hangups --manual-login` in shell
3. Use ctrl+e to exit hangups after logging in and run `hangups --log path-to-logfile -d` to setup logging
4. Put your Discord webhook url into an environmental variable called 'WEBHOOK'

Parses the logging info (event_notification) to send messages to Discord.
