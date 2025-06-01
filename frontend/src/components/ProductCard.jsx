import { Heading, IconButton, Box, Flex, Stack, Card, CardBody, CardFooter, Grid, GridItem, Image, Text } from "@chakra-ui/react";
import { DragHandleIcon, StarIcon, PlusSquareIcon, DeleteIcon } from '@chakra-ui/icons'

const ProductCard = (
    {name,
    in_stock,
    price,
    description}
) => {

    return (
        <Card variant="filled" size="sm">
            <CardBody>
                {/* <Image 
                src={image}
                borderRadius='lg'
                alt={title} 
                fallbackSrc="/images/placeholder.webp" /> */}

                <Stack mt='6' />
                <Heading size='md'>{name}</Heading>
                <Flex justifyContent="space-between" pt={3}>
                    <Text >in stock: {in_stock}</Text>
                    <Text color='blue.600'>Price: {price}</Text>
                </Flex>
            </CardBody>

            

            <CardFooter justifyContent='space-between'>
                <Text >description: {description}</Text>
                <IconButton icon={<StarIcon />} onClick={() => addToOrder(id)} aria-label="Add to order" />
            </CardFooter>
        </Card>
    );
};


export default ProductCard;