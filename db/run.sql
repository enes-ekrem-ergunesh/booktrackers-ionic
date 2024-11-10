CREATE TABLE `users` (
  `id` int,
  `email` varchar(255),
  `password` varchar(255),
  `created_at` timestamp,
  `updated_at` timestamp,
  PRIMARY KEY (`id`)
);

CREATE TABLE `tokens` (
  `id` int,
  `user_id` int,
  `token` varchar(512),
  `valid_until` timestamp,
  `revoked_at` timestamp,
  `created_at` timestamp,
  `updated_at` timestamp,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
);

