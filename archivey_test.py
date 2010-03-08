import unittest
import mock
import archivey 

class TestArchivey(unittest.TestCase):
	def setUp(self):
		self.blips = {}
		for i in range(20):
			blip = mock.Mock(spec=['is_root'])
			blip.name = "blip "+str(i)
			blip.is_root.return_value = False
			blip.last_modified_time = i
			self.blips[blip.name] = blip

		self.wavelet = mock.Mock(spec=['delete'])
		self.wavelet.blips = self.blips

	def callback(self):
		archivey.OnBlipCreated(mock.Mock(), self.wavelet)

	def testArchiveyDeletesAllButFivePosts(self):
		self.callback()
		self.assertEqual(16, self.wavelet.delete.call_count)

	def assertDeletionOrder(self, names):
		for idx, blip_number in enumerate(names):
			name = 'blip '+str(blip_number)
			self.assertEquals(name, self.wavelet.delete.call_args_list[idx][0][0].name)

	def testArchiveyDeletesOldestPostFirst(self):
		self.callback()
		self.assertDeletionOrder([0, 1, 2, 3, 4])

	def testArchiveySortsByLastModTime(self):
		self.blips['blip 2'].last_modified_time = 100
		self.callback()
		self.assertDeletionOrder([0, 1, 3, 4, 5])

	def testDoesNotDeleteRootNote(self):
		self.blips['blip 0'].is_root.return_value = True
		self.callback()
		self.assertDeletionOrder([1, 2, 3, 4, 5])

if __name__ == '__main__':
	unittest.main()
