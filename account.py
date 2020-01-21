from abc import  ABC, abstractmethod
from rest import restBalance

class Account ():

	def __init__ (self, pub_k, pvt_k):
		self._pub_k = pub_k
		self._pvt_k = pvt_k

	@property
	def pub_k (self):
		return self._pub_k
	@pub_k.setter
	def pub_k (self, new_pub):
		self._pub_k = new_pub

	@property
	def pvt_k (self):
		return self._pvt_k
	@pvt_k.setter
	def pvt_k (self, new_pvt):
		self._pvt_k = new_pvt

	def get_balance (self):
		return restBalance (pub_k(self), pvt_k(self))

	def __str__ (self):
		_balance = restBalance (self._pub_k, self._pvt_k)
		return f'Account info:\n public key-> {self._pub_k}\n private key-> {self._pvt_k}\n balance-> {_balance}'

