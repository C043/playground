export function sendWelcomeEmail(user, emailService) {
  if (!user.email) throw new Error("No Email provided")
  return emailService.send({
    to: user.email,
    subject: "Welcome!",
    body: `Hello, ${user.name}!`
  })
}
