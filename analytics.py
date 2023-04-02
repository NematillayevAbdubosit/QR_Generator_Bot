def analytics(func: callable):
	total_messages = 0
	users = set()
	total_users = 0

	def analytics_wrapper(message):
		nonlocal total_messages, total_users
		total_message += 1

		if message.chat.id not in users:
			users.add(message.chat.id)
			total_users += 1
			with open("users_data.txt", 'w') as data:
				data.write("User_name:", "User_link: ", "User_id:")

		print("New message:", message.text, "Total messages:", total_messages, "Total users:", total_users)

		return func(message)
	return analytics_wrapper