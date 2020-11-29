#include <stdio.h>
#include <stdlib.h>

#define DOWN 0
#define UP 1
#define LEFT 2
#define RIGHT 3

#define TARGET_X 7
#define TARGET_Y 4
#define FAVORITE_NR 10

typedef enum MoveStates {INVALID, VALID, TARGET_FOUND};

struct visited_path {
	struct path *the_path;
	struct visited_path next;
};

struct path {
	int x;
	int y;
	struct path *next;
};

struct visited_path *nodes;

int isWall(int x, int y, int favvo_nr) {
	if(x < 0 || y < 0) return 1;

	unsigned int f = x*x + 3*x + 2*x*y + y + y*y;
	f += favvo_nr;

	char *bits = (char *)calloc(33, sizeof(char));
	int bits_set = 0;

	for(int bit = 0; bit < 32; bit++) {
		if(f & (2 << bit)) {
			bits[bit] = '1';
			bits_set++;
		}
	}
	free(bits);
	return bits_set % 2 == 1;
}

int visited(struct path *list, int test_x, int test_y) {
	int found = 0;
	for(struct path *itm = list; !found && itm != NULL; itm = itm->next) {
		if(itm->x == test_x && itm->y == test_y) {
			found = 1;
		}
	}
	return found;
}

MoveStates can_move_to(struct path *visited, int next_x, int next_y) {
	MoveStates state = next_x == TARGET_X && next_y == TARGET_Y ? TARGET_FOUND;

	if(state != TARGET_FOUND) {
		state = !isWall(next_x, next_y) && !visited(visited, next_x, next_y) ? VALID : INVALID;
		state = !isWall(next_x, next_y) && !visited(visited, next_x, next_y) ? VALID : INVALID;
	}
	return state;
}

void add_node(struct visited_path *root, struct path *node) {

}

void add_visited_node(struct path *path_list, struct path *pos) {
	struct *path list = path_list;
	while(list->next != NULL);
	list->next = pos;
}

struct *create_node(int, x, int y) {
	struct path *node = (struct path *)malloc(sizeof(struct path));
	node->x = pos_x;
	node->y = pos_y + 1;
	node->next = NULL;
	return node;
}

int find_path(struct *path current_path, int pos_x, int pos_y) {
	int valid_moves[4] = {0,0,0,0};

	MoveStates next_state;
	struct path *visited = create_node(pos_x, pos_y);

	if((next_state = can_move_to(visited, pos_x , pos_y + 1)) != INVALID) {
		if(next_state == TARGET_FOUND)
			return 1;
		add_node(create_node(pos_x, pos_y + 1));
		return find_path(nodes, )
	}
	return nodes;
}

int main(int argc, char **argv)
{
	int maze[MAX_Y][MAX_X];

	for(int row = 0; row < MAX_Y; row++) {
		for(int col = 0; col < MAX_X; col++) {
			maze[row][col] =  isWall(col, row, FAVORITE_NR);
		}
	}

	nodes = (struct visited_path *)malloc(sizeof(struct visited_path));

	printf("  0123456789\n");
	for(int row = 0; row < 50; row++) {
		printf("%d ", row);
		for(int col = 0; col < 50; col++) {

			printf("%c", maze[row][col] ? '#' : '.');
		}
		printf("\n");
	}
	return 0;
}
