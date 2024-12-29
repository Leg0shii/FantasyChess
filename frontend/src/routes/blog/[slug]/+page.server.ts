import { error } from '@sveltejs/kit';
import { posts } from '../data.js';

export function load({ params }: { params: { slug: string } }) {
    const post = posts.find((post) => post.slug === params.slug);

    if (!post) error(404);
    return {
        post
    };
}