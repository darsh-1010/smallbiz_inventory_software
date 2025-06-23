from plyer import notification

def show_notification(title, message, timeout=5):
    """
    Show a desktop notification.
    
    Args:
        title (str): Notification title.
        message (str): Notification message body.
        timeout (int): Duration to display in seconds (default 5s).
    """
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=timeout
        )
        print(f"[INFO] Notification shown: {title} - {message}")
    except Exception as e:
        print(f"[ERROR] Failed to show notification: {e}")
