import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"
PET_ID = 9876543210

class TestPetStoreAPI:

    def test_create_pet_positive(self):
        payload = {
            "id": PET_ID,
            "category": {"id": 1, "name": "Dogs"},
            "name": "QA_Dog",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "automation"}],
            "status": "available"
        }
        response = requests.post(f"{BASE_URL}/pet", json=payload)
        assert response.status_code == 200
        assert response.json()["name"] == "QA_Dog"

    def test_create_pet_negative_invalid_body(self):
        payload = {"id": "invalid_id_format_for_integer"}
        response = requests.post(f"{BASE_URL}/pet", json=payload)
        assert response.status_code in [400, 500] 

    def test_read_pet_positive(self):
        response = requests.get(f"{BASE_URL}/pet/{PET_ID}")
        assert response.status_code == 200
        assert response.json()["id"] == PET_ID

    def test_read_pet_negative_not_found(self):
        invalid_id = 9999999999999
        response = requests.get(f"{BASE_URL}/pet/{invalid_id}")
        assert response.status_code == 404
        assert response.json()["message"] == "Pet not found"

    def test_update_pet_positive(self):
        payload = {
            "id": PET_ID,
            "name": "QA_Dog_Updated",
            "status": "sold"
        }
        response = requests.put(f"{BASE_URL}/pet", json=payload)
        assert response.status_code == 200
        assert response.json()["name"] == "QA_Dog_Updated"
        assert response.json()["status"] == "sold"

    def test_delete_pet_positive(self):
        response = requests.delete(f"{BASE_URL}/pet/{PET_ID}")
        assert response.status_code == 200

    def test_delete_pet_negative_already_deleted(self):
        response = requests.delete(f"{BASE_URL}/pet/{PET_ID}")
        assert response.status_code == 404
