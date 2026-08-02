# specs.json schema (per robot)

Flat JSON object. Every spec field is an object:
`{"value": <string|number|null>, "confidence": "vendor-claimed|third-party|estimated", "source": "<url>"}`.
Use `null` value when not disclosed. Numbers in SI units named by the key.
Top-level identity fields are plain strings.

```json
{
  "robot": "A2-W",
  "robot_native": "远征A2-W",
  "company": "AgiBot (Zhiyuan Robotics)",
  "company_native": "智元机器人",
  "hq_country": "China",
  "hq_city": "Shanghai",
  "region": "China",
  "status": "shipping",
  "first_shown": "2024",
  "target_applications": "industrial logistics, manufacturing",

  "base_type":            {"value": "wheeled (diff-drive)", "confidence": "", "source": ""},
  "height_mm":            {"value": null, "confidence": "", "source": ""},
  "weight_kg":            {"value": null, "confidence": "", "source": ""},
  "dof_total":            {"value": null, "confidence": "", "source": ""},
  "dof_per_arm":          {"value": null, "confidence": "", "source": ""},
  "reach_mm":             {"value": null, "confidence": "", "source": ""},
  "payload_per_arm_kg":   {"value": null, "confidence": "", "source": ""},
  "payload_total_kg":     {"value": null, "confidence": "", "source": ""},
  "torso_lift":           {"value": "e.g. 400mm lift column / fixed", "confidence": "", "source": ""},
  "max_speed_ms":         {"value": null, "confidence": "", "source": ""},
  "battery_kwh":          {"value": null, "confidence": "", "source": ""},
  "runtime_h":            {"value": null, "confidence": "", "source": ""},
  "actuators":            {"value": "", "confidence": "", "source": ""},
  "end_effector":         {"value": "gripper / dexterous hand, details", "confidence": "", "source": ""},
  "media_at_flange":      {"value": "power/data/pneumatics or n/a", "confidence": "", "source": ""},
  "sensors_head":         {"value": "", "confidence": "", "source": ""},
  "sensors_wrist_hand":   {"value": "", "confidence": "", "source": ""},
  "sensors_base":         {"value": "", "confidence": "", "source": ""},
  "compute":              {"value": "e.g. 2x Jetson AGX Orin", "confidence": "", "source": ""},
  "software_stack":       {"value": "ROS 2 / proprietary; SDK; AI models", "confidence": "", "source": ""},
  "safety_compliance":    {"value": "", "confidence": "", "source": ""},
  "price":                {"value": "e.g. USD 100k / RMB 300k / RaaS $x/mo", "confidence": "", "source": ""},
  "availability":         {"value": "", "confidence": "", "source": ""},
  "deployment_evidence":  {"value": "", "confidence": "", "source": ""},

  "sources": ["url1", "url2"],
  "notes": ""
}
```
