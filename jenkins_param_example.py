import sys

papam, commit_num = sys.argv[1], sys.argv[2]
file_name  = 'artifact_' + papam + '_' + commit_num + '.txt'
file_hand  = open(file_name, 'w')
file_hand.write('Build: ' + papam + commit_num)
file_hand.close()
