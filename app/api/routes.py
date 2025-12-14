from fastapi import APIRouter
from pathlib import Path
import json

router = APIRouter()
DATA_PATH = Path("app/data/dummy_onboarding.json")

def load_dummy():
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))

@router.get("/dummy/onboarding")
def get_dummy_onboarding():
    # 50 user listesi döner
    return load_dummy()

@router.get("/dummy/onboarding/user")
def get_dummy_user(user_id: int):
    # tek user döner
    data = load_dummy()
    for u in data:
        if u["user_id"] == user_id:
            return u
    return {}

@router.get("/dummy/brand_choices")
def get_dummy_brand_choices():
    # flat list: ALS/segment için en kullanışlı format
    data = load_dummy()
    out = []
    for u in data:
        uid = u["user_id"]
        for b in u["brand_choices"]:
            out.append({
                "user_id": uid,
                "brand_id": b["brand_id"],
                "slot_position": b["slot_position"],
                "slot_score": b["slot_score"]
            })
    return out

@router.get("/dummy/reward_choices")
def get_dummy_reward_choices():
    data = load_dummy()
    out = []
    for u in data:
        uid = u["user_id"]
        for r in u["reward_choices"]:
            out.append({
                "user_id": uid,
                "reward_id": r["reward_id"],
                "slot_position": r["slot_position"],
                "slot_score": r["slot_score"]
            })
    return out
