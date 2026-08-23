import Image from "next/image";

export default function Logo({ className = "" }: { className?: string }) {
  return (
    <div className={`flex items-center gap-2 ${className}`}>
      <Image
        src="/logo.png"
        alt="QuestIDE"
        width={28}
        height={28}
        priority
        className="object-contain"
      />
      <span className="hidden sm:inline font-bold tracking-tight text-zinc-100 font-sans">
        QuestIDE
      </span>
    </div>
  );
}
