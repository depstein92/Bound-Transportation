test_view = """
        <div style="background-color: #707bb2; margin: 15px; border-radius: 5px; padding: 15px; width: 215px">
        <b>Create User:</b>
        <form action="/create-user" method="post">
            <p><input type=text name=user_name placeholder=" username...">
            <p><input type=text name=password placeholder=" password...">
            <p><input type=submit value="Create User">
          	<br>
        </form>
        </div>
        <div style="background-color: #707bb2; margin: 15px; border-radius: 5px; padding: 15px; width: 215px">
        <b>Login:</b>
        <form action="/login-user" method="post">
            <p><input type=text name=user_name placeholder=" username...">
            <p><input type=text name=password placeholder=" password...">
            <p><input type=submit value="Login User">
        </form>
        </div>
        <div style="background-color: #707bb2; margin: 15px; border-radius: 5px; padding: 15px; width: 215px">
        <b>Update User:</b>
        <form action="/update-user" method="post" enctype="multipart/form-data">
            <p>Set Profile Image<input type=file name=file>
            <p>Set Payment Hash<input type=text name=payment_hash placeholder=" payment hash...">
            <p><input type=submit value="Update User">
        </form>
        </div>
        """