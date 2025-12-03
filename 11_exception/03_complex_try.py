def serve_chai(flavor):
    try:
        print(f"Preparing your {flavor} chai...")
        if flavor not in ["masala", "ginger", "elaichi"]:
            raise ValueError("We do not serve this flavor of chai.")
        print(f"Here is your {flavor} chai!")
    except ValueError as e:
        print(e)
serve_chai("mint")  # This will trigger the exception handling
serve_chai("masala")  # This will work fine
