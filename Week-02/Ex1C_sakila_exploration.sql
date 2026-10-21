/*
a) The actor table contains information about actors, including actor_id, first_name, last_name, and last_update.

b) The film table contains information about films, including film_id, title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, and last_update.

c) The film_actor table contains columns for both actor-id and film_id.

d) The rental table includes information about customer rentals such as rental_id, rental_date, inventory_id, customer_id, return-date, staff_id, and last_update. The information is somewhat difficult to read because it contains numeric IDs that reference data stored in other tables.

e) The ineventory table includes information about the copies of films available in stores, including inventory_id, film_id, store_id, and last_update.

f) To find the name of all films rented on a specific date, I would need to use the rental, inventory, and film tables. The rental table records when an item was rented, the inventory table links rentals to specific film copies, and the film table contains the film title. These tables are related through inventory_id and film_id. 
*/

SELECT * FROM rental;

SELECT * FROM inventory;

SELECT * FROM film;