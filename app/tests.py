from django.test import TestCase
from app import models

# Create your tests here.

class TestAirline(TestCase):
    def test_can_create_ticket(self):
        ticket = models.create_ticket(
            "2024-05-01",
            "Manfield",
            "Nathan",
            2,
            False
        )

        self.assertEqual(ticket.id, 1)
        self.assertEqual(ticket.date, "2024-05-01")
        self.assertEqual(ticket.destination, "Manfield")
        self.assertEqual(ticket.passenger, "Nathan")
        self.assertEqual(ticket.bags, 2)
        self.assertFalse(ticket.first_class)


    def test_can_get_all_tickets(self):
        ticket = models.create_ticket(
            "2024-05-01",
            "Manfield",
            "Nathan",
            2,
            False
        )
        ticket2 = models.create_ticket(
            "2024-05-01",
            "Manfield",
            "Nathan",
            2,
            False
        )
        ticket3 = models.create_ticket(
            "2024-05-01",
            "Manfield",
            "Nathan",
            2,
            False
        )

        test_list = models.all_tickets()

        self.assertEqual(len(test_list), 3)

    def test_delete_tickets(self):
        ticket = models.create_ticket(
            "2024-05-01",
            "Manfield",
            "Nathan",
            2,
            False
        )
        ticket2 = models.create_ticket(
            "2024-05-01",
            "Manfield",
            "Nathan",
            2,
            False
        )
        ticket3 = models.create_ticket(
            "2024-05-01",
            "Manfield",
            "Nathan",
            2,
            False
        )
        ticket4 = models.create_ticket(
            "2024-05-01",
            "Manfield",
            "Nathan",
            2,
            False
        )

        tickets = models.all_tickets()

        self.assertEqual(len(tickets), 4)

        models.delete_ticket(2)
        models.delete_ticket(3)

        new = models.all_tickets()

        self.assertNotEqual(tickets, new)
        self.assertEqual(len(new), 2)

    def test_tickets_by_first_class(self):
        ticket = models.create_ticket(
            "2024-05-01",
            "Manfield",
            "Nathan",
            2,
            False
        )
        ticket2 = models.create_ticket(
            "2024-05-01",
            "Manfield",
            "Nathan",
            2,
            False
        )
        ticket3 = models.create_ticket(
            "2024-05-01",
            "Manfield",
            "Nathan",
            2,
            False
        )
        ticket4 = models.create_ticket(
            "2024-05-01",
            "Manfield",
            "Nathan",
            2,
            False
        )

        tickets = models.all_tickets()

        ticket2 = models.upgrade_first_class(2)
        ticket4 = models.upgrade_first_class(4)

        filtered_tickets = models.tickets_by_first_class()

        self.assertNotEqual(tickets, filtered_tickets)
        self.assertEqual(len(filtered_tickets), 2)




