import sys
import traceback
from django.utils import termcolors
from django.core.management.base import LabelCommand

style = termcolors.make_style(fg='green', opts=('bold',))

class Command(LabelCommand):
	help = 'Executes the given Python source file under the context of the current Django settings'
	label = 'filename'
	args = '<filename filename ...>'
	requires_model_validation = False

	def handle_label(self, label, **options):
		sys.stderr.write(style('Executing %s' % label) + '\n')
		try:
			execfile(label, dict(__name__='__main__', __file__=label))
		except Exception as e:
			print "Exception in script:"
			traceback.print_exc(file=sys.stdout)
