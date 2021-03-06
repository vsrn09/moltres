import requests

resp = requests.get('https://cloudpricingcalculator.appspot.com/static/data/pricelist.json').json()


region_dict = {
  'USE1' : 'us-east4',
  'USE2' : 'us-central1',
  'USW1' : 'us-west1',
  'USW2' : 'us-west1',
  'UGE1' : 'us-east1',
  'UGW1' : 'us-west1',
  'CPT' : 'us-central1',
  'APE1' : 'asia-east2',
  'APN1' : 'asia-northeast1',
  'APN2' : 'asia-northeast3',
  'APN3' : 'asia-northeast2',
  'APS1' : 'asia-southeast1',
  'APS2' : 'australia-southeast1',
  'APS3' : 'asia-south1',
  'CAN1' : 'us-central1',
  'EUC1' : 'europe-west3',
  'EUW1' : 'europe-west2',
  'EUW2' : 'europe-west2',
  'EUW3' : 'europe-west1',
  'EUN1' : 'europe-north1',
  'EUS1' : 'europe-west3',
  'MES1' : 'us-central1',
  'SAE1' : 'southamerica-east1',
}

compute_ratecard = {
	'box':{
		'n1-predefined-vcpus' : resp['gcp_price_list']["CP-COMPUTEENGINE-N1-PREDEFINED-VM-CORE"] ,
		'n1-predefined-memory' : resp['gcp_price_list']["CP-COMPUTEENGINE-N1-PREDEFINED-VM-RAM"] ,
		'n1-custom-vcpus' : resp['gcp_price_list']["CP-COMPUTEENGINE-N1-CUSTOM-VM-CORE"] ,
		'n1-custom-memory' : resp['gcp_price_list']["CP-COMPUTEENGINE-N1-CUSTOM-VM-RAM"] ,
		'e2-predefined-vcpus' : resp['gcp_price_list']["CP-COMPUTEENGINE-E2-PREDEFINED-VM-CORE"] ,
		'e2-predefined-memory' : resp['gcp_price_list']["CP-COMPUTEENGINE-E2-PREDEFINED-VM-RAM"] ,
		'e2-micro' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-E2-MICRO"] ,
		'e2-small' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-E2-SMALL"] ,
		'e2-medium' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-E2-MEDIUM"] ,
		'f1-micro' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-F1-MICRO"] ,
		'g1-small' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-G1-SMALL"] ,
	},
	'heavy':{
		'n1-predefined-vcpus' : resp['gcp_price_list']["CP-COMPUTEENGINE-N1-CUD-1-YEAR-CPU"] ,
		'n1-predefined-memory' : resp['gcp_price_list']["CP-COMPUTEENGINE-N1-CUD-1-YEAR-RAM"] ,
		'n1-custom-vcpus' : resp['gcp_price_list']["CP-COMPUTEENGINE-N1-CUSTOM-VM-CORE"] ,
		'n1-custom-memory' : resp['gcp_price_list']["CP-COMPUTEENGINE-N1-CUSTOM-VM-RAM"] ,
		'e2-predefined-vcpus' : resp['gcp_price_list']["CP-COMPUTEENGINE-E2-CUD-1-YEAR-CPU"] ,
		'e2-predefined-memory' : resp['gcp_price_list']["CP-COMPUTEENGINE-E2-CUD-1-YEAR-RAM"] ,
		'e2-micro' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-E2-MICRO"] ,
		'e2-small' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-E2-SMALL"] ,
		'e2-medium' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-E2-MEDIUM"] ,
		'f1-micro' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-F1-MICRO"] ,
		'g1-small' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-G1-SMALL"] ,
	},
	'spot':{
		'n1-predefined-vcpus' : resp['gcp_price_list']["CP-COMPUTEENGINE-N1-PREDEFINED-VM-CORE-PREEMPTIBLE"] ,
		'n1-predefined-memory' : resp['gcp_price_list']["CP-COMPUTEENGINE-N1-PREDEFINED-VM-RAM-PREEMPTIBLE"] ,
		'n1-custom-vcpus' : resp['gcp_price_list']["CP-COMPUTEENGINE-N1-CUSTOM-VM-CORE-PREEMPTIBLE"] ,
		'n1-custom-memory' : resp['gcp_price_list']["CP-COMPUTEENGINE-N1-CUSTOM-VM-RAM-PREEMPTIBLE"] ,
		'e2-predefined-vcpus' : resp['gcp_price_list']["CP-COMPUTEENGINE-E2-PREDEFINED-VM-CORE-PREEMPTIBLE"] ,
		'e2-predefined-memory' : resp['gcp_price_list']["CP-COMPUTEENGINE-E2-PREDEFINED-VM-RAM-PREEMPTIBLE"] ,
		'e2-micro' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-E2-MICRO-PREEMPTIBLE"] ,
		'e2-small' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-E2-SMALL-PREEMPTIBLE"] ,
		'e2-medium' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-E2-MEDIUM-PREEMPTIBLE"] ,
		'f1-micro' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-F1-MICRO-PREEMPTIBLE"] ,
		'g1-small' : resp['gcp_price_list']["CP-COMPUTEENGINE-VMIMAGE-G1-SMALL-PREEMPTIBLE"] ,
	},
}

# persistentdisk_ratecard = {
# 	'snapshot': resp['gcp_price_list']["CP-COMPUTEENGINE-STORAGE-PD-SNAPSHOT"],

# }

persistentdisk_ratecard = {
  'snapshot': {
      "us": 0.026,
      "us-central1": 0.026,
      "us-east1": 0.026,
      "us-east4": 0.029,
      "us-west4": 0.029,
      "us-west1": 0.026,
      "us-west2": 0.031,
      "us-west3": 0.031,
      "europe": 0.026,
      "europe-west1": 0.026,
      "europe-west2": 0.031,
      "europe-west3": 0.031,
      "europe-west4": 0.029,
      "europe-west6": 0.034,
      "europe-north1": 0.029,
      "northamerica-northeast1": 0.029,
      "asia-east": 0.026,
      "asia-east1": 0.026,
      "asia-east2": 0.032,
      "asia-northeast": 0.034,
      "asia-northeast1": 0.034,
      "asia-northeast2": 0.034,
      "asia-northeast3": 0.034,
      "asia-southeast": 0.029,
      "asia-southeast1": 0.029,
      "australia-southeast1": 0.035,
      "australia": 0.035,
      "southamerica-east1": 0.039,
      "asia-south1": 0.031,
      "asia-southeast2": 0.034
    },
  'gp2': {
      "us": 0.1,
      "us-central1": 0.1,
      "us-east1": 0.1,
      "us-east4": 0.11,
      "us-west4": 0.11,
      "us-west1": 0.1,
      "us-west2": 0.12,
      "us-west3": 0.12,
      "europe": 0.1,
      "europe-west1": 0.1,
      "europe-west2": 0.12,
      "europe-west3": 0.12,
      "europe-west4": 0.11,
      "europe-west6": 0.12,
      "europe-north1": 0.11,
      "northamerica-northeast1": 0.11,
      "asia-east": 0.1,
      "asia-east1": 0.1,
      "asia-east2": 0.11,
      "asia-northeast": 0.13,
      "asia-northeast1": 0.13,
      "asia-northeast2": 0.13,
      "asia-northeast3": 0.13,
      "asia-southeast": 0.11,
      "asia-southeast1": 0.11,
      "australia-southeast1": 0.135,
      "australia": 0.135,
      "southamerica-east1": 0.15,
      "asia-south1": 0.12,
      "asia-southeast2": 0.13,
    },
  'magnetic': {
      "us": 0.04,
      "us-central1": 0.04,
      "us-east1": 0.04,
      "us-east4": 0.044,
      "us-west4": 0.044,
      "us-west1": 0.04,
      "us-west2": 0.048,
      "us-west3": 0.048,
      "europe": 0.04,
      "europe-west1": 0.04,
      "europe-west2": 0.048,
      "europe-west3": 0.048,
      "europe-west4": 0.044,
      "europe-west6": 0.052,
      "europe-north1": 0.044,
      "northamerica-northeast1": 0.044,
      "asia-east": 0.04,
      "asia-east1": 0.04,
      "asia-east2": 0.05,
      "asia-northeast": 0.052,
      "asia-northeast1": 0.052,
      "asia-northeast2": 0.052,
      "asia-northeast3": 0.052,
      "asia-southeast": 0.044,
      "asia-southeast1": 0.044,
      "australia-southeast1": 0.054,
      "australia": 0.054,
      "southamerica-east1": 0.06,
      "asia-south1": 0.048,
      "asia-southeast2": 0.052
    },
}

nat_gateway_ratecard = {
	'us-vm-low' : resp['gcp_price_list']["CP-NETWORK-SERVICES-CLOUD-NAT-GATEWAY-UPTIME-LOW-VM-NUMBER"]['us'],
	'us-vm-high' : resp['gcp_price_list']["CP-NETWORK-SERVICES-CLOUD-NAT-GATEWAY-UPTIME-HIGH-VM-NUMBER"]['us'],
	'us-bytes' : resp['gcp_price_list']["CP-NETWORK-SERVICES-CLOUD-NAT-TRAFFIC"]['us'],
}

idle_addresses_ratecard = {
	'us' : resp['gcp_price_list']["CP-NETWORK-SERVICES-IP-ADDRESSES"]['us'],
}

loadbalancer_ratecard = {
  'forwarding_rules' : resp['gcp_price_list']['FORWARDING_RULE_CHARGE_BASE'],
  'forwarding_rules_extra' : resp['gcp_price_list']['FORWARDING_RULE_CHARGE_EXTRA'],
  'ingress' : resp['gcp_price_list']['NETWORK_LOAD_BALANCED_INGRESS'],
}